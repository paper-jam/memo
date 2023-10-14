# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
import sys
import os
import random

# ------------------------------------------------------------------------------------


# ------------ un mot est il un palindrome ?
def estPalindrome(m1):
    return m1 == m1[::-1]


# ------------ méthode de classe
class Voiture():
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

    @classmethod
    def lamborghini(cls):
        return Voiture("Lamborghini", 150000, "rouge")

    @classmethod
    def porsche(cls):
        return Voiture("Porsche", 200000, "noire")


lamborghini = Voiture.lamborghini()
print(lamborghini.prix)
porsche = Voiture.porsche()
print(porsche.prix)






# ------------ dossier parent / dossier fils
fichier_courant = __file__
dossier_parent = os.path.dirname(fichier_courant)
dossier_images = os.path.join(dossier_parent, "images")



# 023 ------------
employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
sum(employes.values())

# 022 ---------- recherche de clé dans un dico avec valeur par defaut pour éviter erreur
employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))



# --------------------------------------------------------------------------------------------------------------


lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
print(phrase.lower().count(lettre_a_chercher))

# --------------------------------------------------------------------------------------------------------------
# quand on pas besoin de l'index sur une itération
import random
     
for _ in range(6):
    nombre = random.choice(range(1, 7))
    print(nombre)


# --------------------------------------------------------------------------------------------------------------
# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
class Chemin:
    def __init__(self, chemin):
        self.chemin = chemin

    def __str__(self):
        return self.chemin
        
    def __add__(self, p):
        return Chemin(self.chemin+"/"+p)

c = Chemin("/Users/john")
composite = c + "dossier" + "test" + "script"
print(composite)

# --------------------------------------------------------------------------------------------------------------

# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
from functools import reduce

class Note:
    
    def __init__(self, valeur_note):
        self.valeur_note = valeur_note
    
    # def __repr__(self):
    #     return f"{self.valeur_note} / 20"

    def __repr__(self):
        return self.valeur_note


class Notes(list):

    def ajouter_note(self, note):
        super().append(note)

    # retourne le nb de note = 20
    def notes_parfaites(self):
        nbNoteSupA20 = sum(map(lambda x: x == 20, [note.valeur_note for note in self]))
        return nbNoteSupA20
    
    # moyenne de toutes les notes
    def moyenne(self):
        return self.somme() / len(self)

    def somme(self):
        somme = reduce(lambda x, y:x+y, [note.valeur_note for note in self])
        return somme


valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
print(sum(valeur_notes))
notes = Notes()


for valeur_note in valeur_notes:
    notes.ajouter_note(note=Note(valeur_note=valeur_note))

print(notes.somme())
print(notes.moyenne())

print(notes.notes_parfaites())

