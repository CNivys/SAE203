
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EtudForm
from . import models
from django.conf import settings


# Create your views here.
def ajout(request):
        form = EtudForm()
        return render(request, 'etudiants/ajout.html', {"form": form})

def traitement(request):
    if request.method == "POST":
        rform = EtudForm(request.POST, request.FILES)
        if rform.is_valid():
            etud = rform.save()
            etud.save()
            return HttpResponseRedirect("/ecole/alletud")
        else:
            return render(request, 'etudiants/ajout.html', {"form" : rform})

def all(request):
    liste = list(models.Etudiant.objects.all())
    for etudiant in liste:
        if etudiant.photo:
            etudiant.photo_url = settings.MEDIA_URL + str(etudiant.photo)
    return render(request,'etudiants/all.html', {"liste" : liste})

def affiche(request, id):
    etud = models.Etudiant.objects.get(pk=id)
    absences = models.Absence.objects.filter(etudiant=etud)
    return render(request,"etudiants/affiche.html",{"etud": etud, "absences": absences})

def update(request, id):
    etud = models.Etudiant.objects.get(pk=id)
    form = EtudForm(etud.dico())
    return render(request, "etudiants/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    if request.method == "POST":
        rform = EtudForm(request.POST, request.FILES)
        if rform.is_valid():
            etud = rform.save(commit=False)
            etud.idetudiant = id
            etud.save()
            return HttpResponseRedirect("/ecole/alletud")
        else:
            return render(request, "etudiants/update.html", {"form":rform, "id": id})

def delete(request, id):
    etud = models.Etudiant.objects.get(pk=id)
    etud.delete()
    return HttpResponseRedirect("/ecole/alletud")
