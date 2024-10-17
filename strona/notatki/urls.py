from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notatek, name='lista_notatek'),
    path('dodaj/', views.dodaj_notatke, name='dodaj_notatke'),
    path('notatka/<int:pk>/', views.szczegoly_notatki, name='szczegoly_notatki'),
    path('notatka/<int:pk>/edytuj/', views.edytuj_notatke, name='edytuj_notatke'),
]
