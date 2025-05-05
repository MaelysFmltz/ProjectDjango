from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('pays/',views.liste_pays, name='liste_pays'),
    path('pays/add/',views.ajouter_pays, name='ajouter_pays'),
    path('pays/<int:id>/edit/',views.modifier_pays, name='modifier_pays'),
    path('pays/<int:id>/delete/',views.supprimer_pays, name='supprimer_pays'),

    path('regions/', views.liste_regions,name = 'liste_regions'),
    path('regions/add/', views.ajouter_region, name='ajouter_region'),
    path('regions/<int:id>/edit/', views.modifier_region, name='modifier_region'),
    path('regions/<int:id>/delete/', views.supprimer_region, name='supprimer_region'),
]