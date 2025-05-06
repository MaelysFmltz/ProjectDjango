from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('pays/',views.liste_pays, name='liste_pays'),
    path('pays/add/',views.ajouter_pays, name='ajouter_pays'),
    path('pays/<int:id>/edit/',views.modifier_pays, name='modifier_pays'),
    path('pays/supprimer/<int:pk>/',views.supprimer_pays, name='supprimer_pays'),
    path('pays/supprimer/', views.supprimer_pays_selection, name='supprimer_pays_selection'),


    path('regions/', views.liste_regions,name = 'liste_regions'),
    path('regions/add/', views.ajouter_region, name='ajouter_region'),
    path('regions/<int:id>/edit/', views.modifier_region, name='modifier_region'),
    path('regions/supprimer/<int:pk>/', views.supprimer_region, name='supprimer_region'),
    path('regions/supprimer/', views.supprimer_region_selection, name='supprimer_region_selection'),

]