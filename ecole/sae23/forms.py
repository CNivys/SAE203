from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms


class EnsForm(ModelForm):
    class Meta:
        model = models.Enseigant
        fields = ('idenseignant','nom', 'prenom', 'email')
        label ={
            'nom': _('nom'),
            'prenom': _('prenom'),
            'email': _('email'),
        }

class GrpForm(ModelForm):
    class Meta:
        model = models.Groupe
        fields = ('nom',)
        label ={
            'nom': _('nom'),
        }

class EtudForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('idetudiant','nom', 'prenom', "email", 'photo', 'groupe')
        label ={
            'nom': _('nom'),
            'prenom': _('prenom'),
            'email': _('email'),
            'photo': _('photo'),
            'groupe': _('groupe'),
        }

class coursForm(ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type" : "date"}))
    class Meta:
        model = models.Cours
        fields = ('idcours','titre_cours', 'date', 'duree', 'enseigant')
        label ={
            'titre_cours': _('Libellé'),
            'date': _('Date'),
            'duree': _('Duree'),
            'enseigant': ('Enseignant'),
        }

class AbsForm(ModelForm):
    class Meta:
        model = models.Absence
        fields = ('idabsence','etudiant', 'cours', 'justifier', 'justification')
        label ={
            'etudiant': _('Etudiant'),
            'cours': _('Cours'),
            'justifier': _('Justifié'),
            'justification': _('Justification'),
        }

class TraitementFichierForm(forms.Form):
    file = forms.FileField()