from django import forms
from .models import Cours, Classe, Filiere, Professeur, Salle, Planning

class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['nom', 'code', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['nom', 'filiere', 'niveau', 'nombre_etudiants']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_etudiants': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['nom', 'code', 'filiere', 'professeur', 'heures_total', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'professeur': forms.TextInput(attrs={'class': 'form-control'}),
            'heures_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = ['cours', 'classe', 'salle', 'date', 'heure_debut', 'heure_fin', 'type_seance']
        widgets = {
            'cours': forms.Select(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'salle': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'heure_debut': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'heure_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'type_seance': forms.Select(attrs={'class': 'form-control'}),
        }

class SalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['nom', 'capacite', 'type_salle', 'equipements']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'capacite': forms.NumberInput(attrs={'class': 'form-control'}),
            'type_salle': forms.Select(attrs={'class': 'form-control'}),
            'equipements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
