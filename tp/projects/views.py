from rest_framework import generics
from .models import ProjetDeRecherche, Chercheur, Publication
from .serializers import ProjetDeRechercheSerializer, ChercheurSerializer, PublicationSerializer
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

