import os
from time import time
from random import randint

cur_dir = os.path.dirname(__file__)
fichier = os.path.join(cur_dir, 'nombres_aleatoires.txt')

a = time()

nombre_aleatoire = ''
l1 = []
for i in range(5000000):
    nombre_aleatoire = randint(0, 9999)
    l1.append(nombre_aleatoire)


listNbre = "\n".join([str(i) for i in l1])


with open(fichier, 'w') as f:
    f.write(listNbre)

b = time()

print('Temps d\'execution: {}'.format(b - a))
