import string

# ---- vérifier mo de passe : 2 nombres, 1 majuscule et 8 caractères
mdp = "3541sfdsd$$$"
if len(mdp) >= 8:
    pass
if len([char for char in mdp if char in string.digits]) >= 2:
    pass
if len([char for char in mdp if char in string.ascii_uppercase]) >= 1:
    pass

if any(char.isupper() for char in mdp):
    pass
if len([char for char in mdp if char.isdigit()]) >= 2:
    pass


# ---------------- autres exemples
sequence = ["a", "b", "c"]
sequence2 = [element.upper() for element in sequence]
print(sequence2)  # ['A', 'B', 'C']

# afficher les nombres pairs : présence d'un test à la fin de la syntaxe
nombres = range(10)
print([nombre for nombre in nombres if nombre % 2 == 0])


# -------- mutiple de 7, mais pas multiple de 3
nombres = [i for i in range(0, 1001) if i % 7 == 0 and i % 3 != 0]

#  ----- recoder la fonction isdigit
all([x in string.digits for x in "51z98"])  # --> false

# -------- comprehensive dictio // refaire qq exo sur python
alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
dico = {i + 1: letter for i, letter in enumerate(alphabet)}
#  {1: 'a', 2: 'b', ....... 24: 'x', 25: 'y', 26: 'z'}

# -------- tri des emplyés selon leur ordre alphabétique
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]
alphabet = string.ascii_lowercase
employes_a_m = [e for e in employes if e[0].lower() in alphabet[:13]]
employes_n_z = [e for e in employes if e[0].lower() in alphabet[13:]]

# -------- recuperer les nombres pairs
nombres = range(50)
nombres_pairs = [x for x in nombres if x % 2 == 0]

# -------- somme de chaque chiffre d'un nombre
nombre = 209812
somme = sum([int(i) for i in str(nombre)])

# -------- nested comprenhension list
x = [[j for j in range(5)] for i in range(3)]
# [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

planets = [["Mercury", "Venus", "Earth"], ["Mars", "Jupiter", "Saturn"], ["Uranus", "Neptune", "Pluto"]]
[planet for sublist in planets for planet in sublist if len(planet) < 6]  # ['Venus', 'Earth', 'Mars', 'Pluto']

# flattening list
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
[val for sublist in matrix for val in sublist]  # -> #  [1, 2, 3, 4, 5, 6, 7, 8, 9]

# nesting loops : higher level loop must be on the left
# [(i,j, k) for i in [1,2] for j in ['pomme','banane',] for k in ['A', 'B']]
# [(1, 'pomme', 'A'), (1, 'pomme', 'B'), (1, 'banane', 'A'), (1, 'banane', 'B'), (2, 'pomme', 'A'), (2, 'pomme', 'B'), (2, 'banane', 'A'), (2, 'banane', 'B')]
