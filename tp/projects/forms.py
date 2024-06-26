from django import forms
from .models import Chercheur, ProjetDeRecherche, Publication

class ChercheurForm(forms.ModelForm):
    class Meta:
        model = Chercheur
        fields = ['nom', 'specialite', 'projets']
class ProjetForm(forms.ModelForm):
    class Meta:
        model = ProjetDeRecherche
        fields = ['titre', 'description', 'date_debut', 'date_fin_prevue', 'chef_de_projet']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin_prevue': forms.DateInput(attrs={'type': 'date'}),
        }
class PublicationForm(forms.ModelForm):
    date_publication = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    )
    class Meta:
        model = Publication
        fields = ['titre', 'contenu', 'date_publication', 'projet_associe']
