from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Filières
    path('filieres/', views.filiere_list, name='filiere_list'),
    path('filieres/create/', views.filiere_create, name='filiere_create'),
    path('filieres/<int:pk>/update/', views.filiere_update, name='filiere_update'),
    
    
    # Classes
    path('classes/', views.classe_list, name='classe_list'),
    path('classes/create/', views.classe_create, name='classe_create'),
    path('classe/<int:pk>/update/', views.classe_create, name='classe_update'),
    
    # Cours
    path('cours/', views.cours_list, name='cours_list'),
    path('cours/create/', views.cours_create, name='cours_create'),
    path('cours/<int:pk>/update/', views.cours_create, name='cours_update'),

    # Salles
    path('salles/', views.salle_list, name='salle_list'),
    path('salles/create/', views.salle_create, name='salle_create'),
    path('salles/<int:pk>/update/', views.salle_create, name='salle_update'),
    
    # Planning
    path('planning/', views.planning_list, name='planning_list'),
    path('planning/create/', views.planning_create, name='planning_create'),
    path('planning/calendar/', views.planning_calendar, name='planning_calendar'),

    
]
