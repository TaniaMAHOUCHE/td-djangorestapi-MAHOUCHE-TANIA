from rest_framework import generics
from .models import ProjetDeRecherche, Chercheur, Publication
from .serializers import ProjetDeRechercheSerializer, ChercheurSerializer, PublicationSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Chercheur, ProjetDeRecherche, Publication
from .forms import ChercheurForm, ProjetForm, PublicationForm
from django.views.generic import ListView

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
    
class ListeProjetsRecherche(ListView):
    model = ProjetDeRecherche
    template_name = 'projets.html' 
    context_object_name = 'projets'  

    def get_queryset(self):
        queryset = super().get_queryset()
        titre_query = self.request.GET.get('titre', '') 
        
        if titre_query:
            queryset = queryset.filter(titre__icontains=titre_query)
        
        return queryset

   
def liste_chercheurs(request):
    chercheurs = Chercheur.objects.all()
    context = {
        'chercheurs': chercheurs
    }
    return render(request, 'chercheurs.html', context)
    
def liste_projets(request):
    projets = ProjetDeRecherche.objects.all()
    return render(request, 'projets.html', {'projets': projets})
       
def bonjour(request):
    return render(request, 'bonjour.html')

def index(request):
    return render(request, 'index.html')

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

def delete_projet(request, pk):
    projet = get_object_or_404(ProjetDeRecherche, pk=pk)
    
    if request.method == 'POST':
        projet.delete()
        return redirect('list_projets') 
    
    return redirect('list_projets')  
    
def update_projet(request, pk):
    projet = get_object_or_404(ProjetDeRecherche, pk=pk)
    
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('list_projets') 
    else:
        form = ProjetForm(instance=projet)
    
    context = {
        'form': form,
        'projet': projet,
    }
    return render(request, 'update_projet.html', context)



def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-publication')  
    else:
        form = PublicationForm()
    
    chercheurs = Chercheur.objects.all()
    
    context = {
        'form': form,
        'chercheurs': chercheurs
    }
    return render(request, 'add_publication.html', context)

def update_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('list-publication') 
    else:
        form = PublicationForm(instance=publication)
    
    chercheurs = Chercheur.objects.all()
    
    context = {
        'form': form,
        'chercheurs': chercheurs
    }
    return render(request, 'update_publication.html', context)

def delete_publication(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    
    if request.method == 'POST':
        publication.delete()
        return redirect('list-publication')  
    
    return redirect('list-publication')  

def lister_publications(request):
    publications = Publication.objects.all()
    titre_search = request.GET.get('titre')
    if titre_search:
        publications = publications.filter(titre__icontains=titre_search)

    context = {
        'publications': publications,
    }
    return render(request, 'publications.html', context)