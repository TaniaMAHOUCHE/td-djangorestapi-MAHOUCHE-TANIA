"""
URL configuration for tp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from projects import views

from projects.views import (
    liste_chercheurs, index, 
    add_chercheur, update_chercheur, delete_chercheur, 
    add_projet, liste_projets, delete_projet, update_projet, 
    lister_publications, add_publication, update_publication, delete_publication
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('', index, name='index'),
    
    path('chercheurs/', liste_chercheurs, name='list_chercheurs'),
    path('add_chercheur/', add_chercheur, name='add_chercheur'),
    path('update_chercheur/<int:chercheur_id>/', update_chercheur, name='update_chercheur'),
    path('delete_chercheur/<int:chercheur_id>/', delete_chercheur, name='delete_chercheur'),  
    
    path('add_projet/', add_projet, name='add_projet'),
    path('projets/', liste_projets, name='list_projets'),
    path('delete_projet/<int:pk>/', delete_projet, name='delete_projet'),
    path('update_projet/<int:pk>/', update_projet, name='update_projet'),
    
    path('publications/', lister_publications, name='list-publication'),
    path('add_publication/', add_publication, name='add-publication'),
    path('update_publication/<int:publication_id>/', update_publication, name='update-publication'),
    path('delete_publication/<int:publication_id>/', delete_publication, name='delete-publication'),
]
