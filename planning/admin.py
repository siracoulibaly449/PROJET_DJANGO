from django.contrib import admin
from .models import Filiere, Classe, Professeur, Salle, Cours, Planning

@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ['nom', 'code', 'description']
    search_fields = ['nom', 'code']

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ['nom', 'filiere', 'niveau', 'nombre_etudiants']
    list_filter = ['filiere', 'niveau']
    search_fields = ['nom']


@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    list_display = ['nom', 'capacite', 'type_salle']
    list_filter = ['type_salle']
    search_fields = ['nom']

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ['nom', 'code', 'filiere', 'professeur', 'heures_total']
    list_filter = ['filiere']
    search_fields = ['nom', 'code']

@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    list_display = ['cours', 'classe', 'salle', 'date', 'heure_debut', 'heure_fin', 'type_seance']
    list_filter = ['date', 'type_seance', 'cours__filiere']
    search_fields = ['cours__nom', 'classe__nom']
    date_hierarchy = 'date'