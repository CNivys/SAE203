from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import GrpForm
from . import models


# Create your views here.
def ajout(request):
        form = GrpForm()
        return render(request, 'groupe/ajout.html', {"form": form})

def traitement(request):
    rform = GrpForm(request.POST)
    if rform.is_valid():
        grp = rform.save()
        grp.save()
        return HttpResponseRedirect("/ecole/allgrp")
    else:
        return render(request, 'groupe/ajout.html', {"form" : rform})

def all(request):
    liste = list(models.Groupe.objects.all())
    return render(request,'groupe/all.html', {"liste" : liste})

def affiche(request, id):
    grp = models.Groupe.objects.get(pk=id)
    etudiants = models.Etudiant.objects.filter(groupe=grp)
    return render(request, "groupe/affiche.html", {"grp": grp, "etudiants": etudiants})

def update(request, id):
    grp = models.Groupe.objects.get(pk=id)
    form = GrpForm(grp.dico())
    return render(request, "groupe/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    rform = GrpForm(request.POST)
    if rform.is_valid():
        grp = rform.save(commit=False)
        grp.idgroupe = id
        grp.save()
        return HttpResponseRedirect("/ecole/allgrp")
    else:
        return render(request, "groupe/update.html", {"form":rform, "id": id})

def delete(request, id):
    grp = models.Groupe.objects.get(pk=id)
    grp.delete()
    return HttpResponseRedirect("/ecole/allgrp")