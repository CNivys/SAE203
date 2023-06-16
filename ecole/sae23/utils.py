from .models import Absence

def ajouter_absences_depuis_fichier(file):
    for line in file:
        line = line.decode('utf-8')
        justifier, idetudiant, idcours = line.strip().split(',')
        absence = Absence(
            justifier=bool(int(justifier)),
            etudiant_id=int(idetudiant),
            cours_id=int(idcours),
        )
        absence.save()
