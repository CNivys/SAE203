from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AbsForm, TraitementFichierForm
from . import models
from .utils import ajouter_absences_depuis_fichier

# Create your views here.
def ajout(request):
        form = AbsForm()
        return render(request, 'absence/ajout.html', {"form": form})

def traitement(request):
    if request.method == "POST":
        rform = AbsForm(request.POST, request.FILES)
        if rform.is_valid():
            abs = rform.save()
            if 'justification' in request.FILES:
                abs.justifier = True
            else:
                abs.justifier = False
            abs.save()
            return HttpResponseRedirect("/ecole/allabs")
        else:
            return render(request, 'absence/ajout.html', {"form" : rform})

def all(request):
    liste = list(models.Absence.objects.all())
    return render(request,'absence/all.html', {"liste" : liste})

def affiche(request, id):
    abs = models.Absence.objects.get(pk=id)
    return render(request,"absence/affiche.html", {"abs": abs})

def update(request, id):
    abs = models.Absence.objects.get(pk=id)
    form = AbsForm(abs.dico())
    return render(request, "absence/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    rform = AbsForm(request.POST)
    if rform.is_valid():
        abs = rform.save(commit=False)
        if 'justification' in request.FILES:
            abs.justifier = True
        else:
            abs.justifier = False
        abs.idabsence = id
        abs.save()
        return HttpResponseRedirect("/ecole/allabs")
    else:
        return render(request, "absence/update.html", {"form":rform, "id": id})

def delete(request, id):
    abs = models.Absence.objects.get(pk=id)
    abs.delete()
    return HttpResponseRedirect("/ecole/allabs")

def selectionner_fichier(request):
    form = TraitementFichierForm()
    return render(request, 'absence/selection_fichier.html', {'form': form})
def traitement_fichier(request):
    if request.method == 'POST':
        file = request.FILES['file']
        ajouter_absences_depuis_fichier(file)
        return HttpResponseRedirect('/ecole/allabs')
    return render(request, 'absence/selection_fichier.html')