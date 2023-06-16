from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import coursForm
from . import models


# Create your views here.
def ajout(request):
        form = coursForm()
        return render(request, 'cours/ajout.html', {"form": form})

def traitement(request):
    rform = coursForm(request.POST)
    if rform.is_valid():
        cours = rform.save()
        cours.save()
        return HttpResponseRedirect("/ecole/allcours")
    else:
        return render(request, 'cours/ajout.html', {"form" : rform})


def all(request):
    liste = list(models.Cours.objects.all())
    return render(request,'cours/all.html', {"liste" : liste})

def affiche(request, id):
    cours = models.Cours.objects.get(pk=id)
    absences = models.Absence.objects.filter(cours=cours)
    return render(request, "cours/affiche.html", {"cours": cours, "absences": absences})

def update(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = coursForm(cours.dico())
    return render(request, "cours/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    rform = coursForm(request.POST)
    if rform.is_valid():
        cours = rform.save(commit=False)
        cours.idcours = id
        cours.save()
        return HttpResponseRedirect("/ecole/allcours")
    else:
        return render(request, "cours/update.html", {"form":rform, "id": id})

def delete(request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("/ecole/allcours")