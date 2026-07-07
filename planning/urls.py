from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Filières
    path('filieres/', views.filiere_list, name='filiere_list'),
    path('filieres/create/', views.filiere_create, name='filiere_create'),
    path('filieres/<int:pk>/update/', views.filiere_update, name='filiere_update'),
    path('filieres/<int:pk>/', views.filiere_detail, name='filiere_detail'),
    path('filieres/<int:pk>/delete/', views.filiere_delete, name='filiere_delete'),
    
    # Classes
    path('classes/', views.classe_list, name='classe_list'),
    path('classes/create/', views.classe_create, name='classe_create'),
    path('classes/<int:pk>/update/', views.classe_update, name='classe_update'),
    path('classes/<int:pk>/', views.classe_detail, name='classe_detail'),
    path('classes/<int:pk>/delete/', views.classe_delete, name='classe_delete'),
    
    # Cours
    path('cours/', views.cours_list, name='cours_list'),
    path('cours/create/', views.cours_create, name='cours_create'),
    path('cours/<int:pk>/update/', views.cours_update, name='cours_update'),
    path('cours/<int:pk>/', views.cours_detail, name='cours_detail'),
    path('cours/<int:pk>/delete/', views.cours_delete, name='cours_delete'),

    # Salles
    path('salles/', views.salle_list, name='salle_list'),
    path('salles/create/', views.salle_create, name='salle_create'),
    path('salles/<int:pk>/update/', views.salle_update, name='salle_update'),
    path('salles/<int:pk>/', views.salle_detail, name='salle_detail'),
    path('salles/<int:pk>/delete/', views.salle_delete, name='salle_delete'),
    
    # Planning
    path('planning/', views.planning_list, name='planning_list'),
    path('planning/create/', views.planning_create, name='planning_create'),
    path('planning/<int:pk>/update/', views.planning_update, name='planning_update'),
    path('planning/<int:pk>/', views.planning_detail, name='planning_detail'),
    path('planning/<int:pk>/delete/', views.planning_delete, name='planning_delete'),
    path('planning/calendar/', views.planning_calendar, name='planning_calendar'),


    
]
