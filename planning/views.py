from django.shortcuts import render, get_object_or_404, redirect
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
    return render(request, 'planning/filiere_form.html', {'form': form, 'title': 'Créer une filière'})

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
    return render(request, 'planning/filiere_form.html', {'form': form, 'title': 'Modifier la filière'})

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
    return render(request, 'planning/classe_form.html', {'form': form, 'title': 'Créer une classe'})

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
    return render(request, 'planning/cours_form.html', {'form': form, 'title': 'Créer un cours'})

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
    return render(request, 'planning/salle_form.html', {'form': form, 'title': 'Créer une salle'})

# Vues pour le Planning
def planning_list(request):
    plannings = Planning.objects.select_related('cours', 'classe', 'salle', 'cours__professeur__user').order_by('-date', '-heure_debut')
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
    return render(request, 'planning/planning_form.html', {'form': form, 'title': 'Créer un planning'})

def planning_calendar(request):
    """Vue calendrier du planning"""
    plannings = Planning.objects.select_related('cours', 'classe', 'salle').filter(
        date__gte=timezone.now().date()
    ).order_by('date', 'heure_debut')
    

    # Organiser par date
    planning_by_date = {}
    for planning in plannings:
        date_str = planning.date.strftime('%Y-%m-%d')
        if date_str not in planning_by_date:
            planning_by_date[date_str] = []
        planning_by_date[date_str].append(planning)
    
    return render(request, 'planning/planning_calendar.html', {'planning_by_date': planning_by_date})
