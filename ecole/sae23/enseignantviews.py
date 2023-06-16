from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EnsForm
from . import models


# Create your views here.
def ajout(request):
        form = EnsForm()
        return render(request, 'enseignants/ajout.html', {"form": form})

def traitement(request):
    rform = EnsForm(request.POST)
    if rform.is_valid():
        ens = rform.save()
        ens.save()
        return HttpResponseRedirect("/ecole/allens")
    else:
        return render(request, 'enseinants/ajout.html', {"form" : rform})

def all(request):
    liste = list(models.Enseigant.objects.all())
    return render(request, 'enseignants/all.html', {"liste": liste})

def affiche(request, id):
    ens = models.Enseigant.objects.get(pk=id)
    cours = models.Cours.objects.filter(enseigant=ens)
    return render(request,"enseignants/affiche.html", {"ens": ens, "cours":cours})

def update(request, id):
    ens = models.Enseigant.objects.get(pk=id)
    form = EnsForm(ens.dico())
    return render(request, "enseignants/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    rform = EnsForm(request.POST)
    if rform.is_valid():
        ens = rform.save(commit=False)
        ens.idenseignant = id
        ens.save()
        return HttpResponseRedirect("/ecole/allens")
    else:
        return render(request, "enseignants/updaterens.html", {"form":rform, "id": id})

def delete(request, id):
    ens = models.Enseigant.objects.get(pk=id)
    ens.delete()
    return HttpResponseRedirect("/ecole/allens")