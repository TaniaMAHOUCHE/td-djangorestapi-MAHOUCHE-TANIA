from rest_framework import generics
from .models import ProjetDeRecherche, Chercheur, Publication
from .serializers import ProjetDeRechercheSerializer, ChercheurSerializer, PublicationSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chercheur
from .forms import ChercheurForm

# Create your views here.
class ProjetDeRechercheListCreate(generics.ListCreateAPIView):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

class ProjetDeRechercheRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjetDeRecherche.objects.all()
    serializer_class = ProjetDeRechercheSerializer

class ChercheurListCreate(generics.ListCreateAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class ChercheurRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chercheur.objects.all()
    serializer_class = ChercheurSerializer

class PublicationListCreate(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class PublicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    
# def liste_chercheurs(request):
#     chercheurs = Chercheur.objects.all()
#     return render(request, 'chercheurs.html', {'chercheurs': chercheurs})

# def chercheurs(request):
#     return render(request, 'chercheurs.html')

def liste_chercheurs(request):
    chercheurs = Chercheur.objects.all()
    context = {
        'chercheurs': chercheurs
    }
    return render(request, 'chercheurs.html', context)

def bonjour(request):
    return render(request, 'bonjour.html')

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render, redirect
from .models import Chercheur
from .forms import ChercheurForm  

from .models import ProjetDeRecherche
from .forms import ProjetForm

def add_chercheur(request):
    if request.method == 'POST':
        form = ChercheurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_chercheurs') 
    else:
        form = ChercheurForm()
    
    context = {
        'form': form
    }
    return render(request, 'add_chercheur.html', context)


def update_chercheur(request, chercheur_id):
    chercheur = get_object_or_404(Chercheur, pk=chercheur_id)

    if request.method == 'POST':
        form = ChercheurForm(request.POST, instance=chercheur)
        if form.is_valid():
            form.save()
            return redirect('list_chercheurs') 
    else:
        form = ChercheurForm(instance=chercheur)
    
    context = {
        'form': form
    }
    return render(request, 'update_chercheur.html', context)

# def delete_chercheur(request, chercheur_id):
#     chercheur = get_object_or_404(Chercheur, pk=chercheur_id)
#     if request.method == 'POST':
#         chercheur.delete()
#         return redirect('list_chercheurs') 
#     return redirect('list_chercheurs')

def delete_chercheur(request, chercheur_id):
    chercheur = get_object_or_404(Chercheur, pk=chercheur_id)
    chercheur.delete()
    return redirect('list_chercheurs')

def add_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_projets') 
    else:
        form = ProjetForm()
    
    context = {
        'form': form
    }
    return render(request, 'add_projet.html', context)
