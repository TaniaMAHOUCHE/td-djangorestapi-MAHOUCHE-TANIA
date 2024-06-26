from django.urls import path
from . import views

urlpatterns = [
    path('projets/', views.ProjetDeRechercheListCreate.as_view(), name='projet-liste-creation'),
    path('projets/<int:pk>/', views.ProjetDeRechercheRetrieveUpdateDestroy.as_view(), name='projet-detail'),
    path('chercheurs/', views.ChercheurListCreate.as_view(), name='chercheur-liste-creation'),
    path('chercheurs/<int:pk>/', views.ChercheurRetrieveUpdateDestroy.as_view(), name='chercheur-detail'),
    path('publications/', views.PublicationListCreate.as_view(), name='publication-liste-creation'),
    path('publications/<int:pk>/', views.PublicationRetrieveUpdateDestroy.as_view(), name='publication-detail'),
]
