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
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from projects.views import liste_chercheurs, bonjour, index, add_chercheur, update_chercheur, delete_chercheur, add_projet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    # path('chercheurs/', views.liste_chercheurs, name='list_chercheurs'),
    path('chercheurs/', liste_chercheurs, name='list_chercheurs'),  
    path('bonjour/', bonjour, name='bonjour'), 
    path('', index, name='index'),
    path('add_chercheur/', add_chercheur, name='add_chercheur'),
    path('update_chercheur/<int:chercheur_id>/', update_chercheur, name='update_chercheur'),
    path('delete_chercheur/<int:chercheur_id>/', delete_chercheur, name='delete_chercheur'),  
    path('add_projet/', add_projet, name='add_projet'),
]
