# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
import string
import random

# ------ génération d'un octet
int("".join(random.choices(["0", "1"], k=8)))


# ----- génération d'un mot de passe, avec une boucle intégré
symboles = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = "".join(random.choice(symboles) for _ in range(20))


# -- ====== random shuffle -> ne fonctionne pas sur une str directement
mot = "Bonjour"
mot = list(mot)
random.shuffle(mot)

# on peut utiliser sample, mais il faut "joiner"
print("".join(random.sample(mot, len(mot))).title())


# -- ===== random , shuffle
from random import randint, shuffle

# génère un nombre aléatoire entre 0 et 1000
x = randint(0, 1000)

# affiche la liste dans le désordre
l1 = [1, 2, 3, 4, 5, 6]
shuffle(l1)  # [5, 4, 3, 6, 2, 1]


# generation d'un uuid avec random
def new_func():
    uuid = "".join(random.sample(string.digits + string.ascii_letters, 15))
