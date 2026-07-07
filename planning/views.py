from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import *
from .forms import *


def dashboard(request):
    """Tableau de bord principal"""
    context = {
        'total_cours': Cours.objects.count(),
        'total_classes': Classe.objects.count(),
        'total_filieres': Filiere.objects.count(),
        'total_salles': Salle.objects.count(),
        'plannings_aujourdhui': Planning.objects.filter(date=timezone.now().date()).count(),
        'plannings_semaine': Planning.objects.filter(
            date__range=[timezone.now().date(), timezone.now().date() + timedelta(days=7)]
        ).count(),
        'recent_plannings': Planning.objects.select_related('cours', 'classe', 'salle').order_by('-date', '-heure_debut')[:5],
    }
    return render(request, 'planning/dashboard.html', context)

# Vues pour les Filières
def filiere_list(request):
    filieres = Filiere.objects.annotate(nb_classes=Count('classe')).all()
    return render(request, 'planning/filiere_list.html', {'filieres': filieres})

def filiere_create(request):
    if request.method == 'POST':
        form = FiliereForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filière créée avec succès!')
            return redirect('filiere_list')
    else:
        form = FiliereForm()
    return render(request, 'planning/filiere_form.html', {
        'form': form,
        'title': 'Créer une filière',
        'cancel_url': reverse('filiere_list'),
    })

def filiere_update(request, pk):
    filiere = get_object_or_404(Filiere, pk=pk)
    if request.method == 'POST':
        form = FiliereForm(request.POST, instance=filiere)
        if form.is_valid():
            form.save()
            messages.success(request, 'Filière modifiée avec succès!')
            return redirect('filiere_list')
    else:
        form = FiliereForm(instance=filiere)
    return render(request, 'planning/filiere_form.html', {
        'form': form,
        'title': 'Modifier la filière',
        'cancel_url': reverse('filiere_list'),
    })

def filiere_detail(request, pk):
    filiere = get_object_or_404(Filiere, pk=pk)
    fields = [
        {'label': 'Nom', 'value': filiere.nom},
        {'label': 'Code', 'value': filiere.code},
        {'label': 'Description', 'value': filiere.description or '—'},
        {'label': 'Nombre de classes', 'value': filiere.classe_set.count()},
    ]
    return render(request, 'planning/detail.html', {
        'title': 'Détails de la filière',
        'fields': fields,
        'list_url': reverse('filiere_list'),
    })

def filiere_delete(request, pk):
    filiere = get_object_or_404(Filiere, pk=pk)
    if request.method == 'POST':
        filiere.delete()
        messages.success(request, 'Filière supprimée avec succès!')
        return redirect('filiere_list')
    return render(request, 'planning/confirm_delete.html', {
        'title': 'Supprimer la filière',
        'object_name': filiere.nom,
        'cancel_url': reverse('filiere_list'),
    })

# Vues pour les Classes
def classe_list(request):
    classes = Classe.objects.select_related('filiere').all()
    return render(request, 'planning/classe_list.html', {'classes': classes})

def classe_create(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classe créée avec succès!')
            return redirect('classe_list')
    else:
        form = ClasseForm()
    return render(request, 'planning/classe_form.html', {
        'form': form,
        'title': 'Créer une classe',
        'cancel_url': reverse('classe_list'),
    })

def classe_update(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classe modifiée avec succès!')
            return redirect('classe_list')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'planning/classe_form.html', {
        'form': form,
        'title': 'Modifier la classe',
        'cancel_url': reverse('classe_list'),
    })

def classe_detail(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    fields = [
        {'label': 'Nom', 'value': classe.nom},
        {'label': 'Filière', 'value': classe.filiere.nom},
        {'label': 'Niveau', 'value': classe.niveau},
        {'label': 'Nombre d\'étudiants', 'value': classe.nombre_etudiants},
    ]
    return render(request, 'planning/detail.html', {
        'title': 'Détails de la classe',
        'fields': fields,
        'list_url': reverse('classe_list'),
    })

def classe_delete(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        messages.success(request, 'Classe supprimée avec succès!')
        return redirect('classe_list')
    return render(request, 'planning/confirm_delete.html', {
        'title': 'Supprimer la classe',
        'object_name': classe.nom,
        'cancel_url': reverse('classe_list'),
    })

# Vues pour les Cours
def cours_list(request):
    cours = Cours.objects.select_related('filiere').all()
    return render(request, 'planning/cours_list.html', {'cours': cours})

def cours_create(request):
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cours créé avec succès!')
            return redirect('cours_list')
    else:
        form = CoursForm()
    return render(request, 'planning/cours_form.html', {
        'form': form,
        'title': 'Créer un cours',
        'cancel_url': reverse('cours_list'),
    })

def cours_update(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cours modifié avec succès!')
            return redirect('cours_list')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'planning/cours_form.html', {
        'form': form,
        'title': 'Modifier le cours',
        'cancel_url': reverse('cours_list'),
    })

def cours_detail(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    fields = [
        {'label': 'Nom', 'value': cours.nom},
        {'label': 'Code', 'value': cours.code},
        {'label': 'Filière', 'value': cours.filiere.nom},
        {'label': 'Professeur', 'value': cours.professeur},
        {'label': 'Heures totales', 'value': cours.heures_total},
        {'label': 'Description', 'value': cours.description or '—'},
    ]
    return render(request, 'planning/detail.html', {
        'title': 'Détails du cours',
        'fields': fields,
        'list_url': reverse('cours_list'),
    })

def cours_delete(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        messages.success(request, 'Cours supprimé avec succès!')
        return redirect('cours_list')
    return render(request, 'planning/confirm_delete.html', {
        'title': 'Supprimer le cours',
        'object_name': cours.nom,
        'cancel_url': reverse('cours_list'),
    })

# Vues pour les Salles
def salle_list(request):
    salles = Salle.objects.all()
    return render(request, 'planning/salle_list.html', {'salles': salles})

def salle_create(request):
    if request.method == 'POST':
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salle créée avec succès!')
            return redirect('salle_list')
    else:
        form = SalleForm()
    return render(request, 'planning/salle_form.html', {
        'form': form,
        'title': 'Créer une salle',
        'cancel_url': reverse('salle_list'),
    })

def salle_update(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    if request.method == 'POST':
        form = SalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Salle modifiée avec succès!')
            return redirect('salle_list')
    else:
        form = SalleForm(instance=salle)
    return render(request, 'planning/salle_form.html', {
        'form': form,
        'title': 'Modifier la salle',
        'cancel_url': reverse('salle_list'),
    })

def salle_detail(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    fields = [
        {'label': 'Nom', 'value': salle.nom},
        {'label': 'Type', 'value': salle.type_salle},
        {'label': 'Capacité', 'value': salle.capacite},
        {'label': 'Equipements', 'value': salle.equipements or '—'},
    ]
    return render(request, 'planning/detail.html', {
        'title': 'Détails de la salle',
        'fields': fields,
        'list_url': reverse('salle_list'),
    })

def salle_delete(request, pk):
    salle = get_object_or_404(Salle, pk=pk)
    if request.method == 'POST':
        salle.delete()
        messages.success(request, 'Salle supprimée avec succès!')
        return redirect('salle_list')
    return render(request, 'planning/confirm_delete.html', {
        'title': 'Supprimer la salle',
        'object_name': salle.nom,
        'cancel_url': reverse('salle_list'),
    })

# Vues pour le Planning
def planning_list(request):
    plannings = Planning.objects.select_related('cours', 'classe', 'salle').order_by('-date', '-heure_debut')
    return render(request, 'planning/planning_list.html', {'plannings': plannings})

def planning_create(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Planning créé avec succès!')
                return redirect('planning_list')
            except Exception as e:
                messages.error(request, f'Erreur: {str(e)}')
    else:
        form = PlanningForm()
    return render(request, 'planning/planning_form.html', {
        'form': form,
        'title': 'Créer un planning',
        'cancel_url': reverse('planning_list'),
    })

def planning_update(request, pk):
    planning = get_object_or_404(Planning, pk=pk)
    if request.method == 'POST':
        form = PlanningForm(request.POST, instance=planning)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Planning modifié avec succès!')
                return redirect('planning_list')
            except Exception as e:
                messages.error(request, f'Erreur: {str(e)}')
    else:
        form = PlanningForm(instance=planning)
    return render(request, 'planning/planning_form.html', {
        'form': form,
        'title': 'Modifier le planning',
        'cancel_url': reverse('planning_list'),
    })

def planning_detail(request, pk):
    planning = get_object_or_404(Planning, pk=pk)
    fields = [
        {'label': 'Cours', 'value': planning.cours.nom},
        {'label': 'Classe', 'value': planning.classe.nom},
        {'label': 'Salle', 'value': planning.salle.nom},
        {'label': 'Date', 'value': planning.date},
        {'label': 'Heure début', 'value': planning.heure_debut},
        {'label': 'Heure fin', 'value': planning.heure_fin},
        {'label': 'Type de séance', 'value': planning.type_seance},
    ]
    return render(request, 'planning/detail.html', {
        'title': 'Détails du planning',
        'fields': fields,
        'list_url': reverse('planning_list'),
    })

def planning_delete(request, pk):
    planning = get_object_or_404(Planning, pk=pk)
    if request.method == 'POST':
        planning.delete()
        messages.success(request, 'Planning supprimé avec succès!')
        return redirect('planning_list')
    return render(request, 'planning/confirm_delete.html', {
        'title': 'Supprimer le planning',
        'object_name': f'{planning.cours.nom} - {planning.classe.nom} - {planning.date}',
        'cancel_url': reverse('planning_list'),
    })


def planning_calendar(request):
    """Vue calendrier hebdomadaire du planning"""
    # Déterminer le lundi de la semaine à afficher (via ?week=+1 / -1 ou une date)
    today = timezone.now().date()
    week_offset = int(request.GET.get('week', 0))
    start_of_week = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)
    end_of_week = start_of_week + timedelta(days=6)

    plannings = Planning.objects.select_related('cours', 'classe', 'salle').filter(
        date__range=[start_of_week, end_of_week]
    ).order_by('date', 'heure_debut')

    # Construire les 7 jours de la semaine, chacun avec sa liste de cours
    jours = []
    for i in range(7):
        jour_date = start_of_week + timedelta(days=i)
        jours.append({
            'date': jour_date,
            'plannings': [p for p in plannings if p.date == jour_date],
        })

    context = {
        'jours': jours,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
        'week_offset': week_offset,
    }
    return render(request, 'planning/planning_calendar.html', context)