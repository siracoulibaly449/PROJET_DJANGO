from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware:
    """Redirige vers la page de connexion si l'utilisateur n'est pas authentifié,
    sauf pour les pages explicitement publiques (login, admin, static)."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_paths = [
            reverse('login'),
            '/admin/',
        ]
        path_is_public = any(request.path.startswith(p) for p in public_paths) or request.path.startswith('/static/')

        if not request.user.is_authenticated and not path_is_public:
            login_url = reverse('login')
            return redirect(f'{login_url}?next={request.path}')

        return self.get_response(request)