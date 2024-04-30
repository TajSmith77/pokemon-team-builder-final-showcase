from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('pokemon/', views.pokemon, name='pokemon'),
    path('pokemon/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]