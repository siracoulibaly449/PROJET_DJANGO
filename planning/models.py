from django.db import models
from django.contrib.auth.models import User

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = "Filière"

class Classe(models.Model):
    nom = models.CharField(max_length=50)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    niveau = models.CharField(max_length=20)
    nombre_etudiants = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nom} - {self.filiere.nom}"

class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20, blank=True)
    specialite = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Salle(models.Model):
    nom = models.CharField(max_length=50)
    capacite = models.IntegerField()
    type_salle = models.CharField(max_length=50, choices=[
        ('COURS', 'Cours magistral'),
        ('TP', 'Travaux pratiques'),
        ('TD', 'Travaux dirigés'),
        ('AMPHI', 'Amphithéâtre'),
    ])
    equipements = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    professeur = models.CharField(max_length=100)
    heures_total = models.IntegerField(help_text="Nombre d'heures total du cours")
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nom} ({self.code})"

class Planning(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    type_seance = models.CharField(max_length=10, choices=[
        ('COURS', 'Cours'),
        ('TD', 'TD'),
        ('TP', 'TP'),
        ('EXAM', 'Examen'),
    ])
    
    class Meta:
        unique_together = [
            ['salle', 'date', 'heure_debut'],
            ['cours', 'date', 'heure_debut'],
        ]
    
    def __str__(self):
        return f"{self.cours.nom} - {self.classe.nom} - {self.date}"
    
    @property
    def professeur(self):
        return self.cours.professeur