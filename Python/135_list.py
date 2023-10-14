# -- ================= LIST

# les listes :  mutable !, tableaux d'éléments hétérogènes indexés
l1 = []
l1 = list()
l1 = ['abc','def',] # comma is allowed
l1 = ['abc',1, 1.0, (12,20,), {'a':1}, {'apple',}, ['a','b',], None, True, ]

# -- ===== accessing with SLICING
# ---- attention dans le slice ou le range, la borne sup est exclue
#  str_object[start_pos:end_pos:step]
#  start_pos is optionnal, default 0
#  end pos is optional, defaut len
#  step optionnal

# attention : Index error si index inexistant
l1 = ["a", "b", "c", "d", "e", "f"]
l1[:]  # toute la liste
l1[0]  # premier element 'a'
l1[-1]  # dernier element 'f'

# slicing : pas d'erreur si les index sont mauvais
l1[1:2]  # 'b' (l'indice superieur est exclu !)
l1[:3]  # 3 premiers elements
l1[3:]  # tous sauf les 3 premiers
l1[-2:-1]  # 'e'
l1[-2:]  # 2 derniers élements 'e', 'f'
l1[:]  # totalité
l1[3:3]  # [] vide

l1[::-1]  # à l'envers ['f', 'e', 'd', 'c', 'b', 'a']
l1.index("c", 2)  # recherche le premier 'c' depuis la pos. 2 incluse

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ma_liste[::2]

# creating list from string
list('abcdef') # ['a', 'b', 'c', 'd', 'e', 'f']


# ------ adding items
l1 = list()
l1.append("Lundi")  # add at the end
l1.insert(4, "Vendredi")  # insère avant l'élément d'indice 4 - aucune erreur en cas de mauvais index
l1.extend(["Samedi", "Dimanche"])  # ajoute normalement 2 éléments - extend prend en param un iterable
l1.extend("ABC")  # !! va ajouter 3 items : 'A', 'B', 'C'
l1.insert(-2, 200)  # donc insère 200 avant l'avant-dernière position
l1 = ["a", "b"]
l2 = ["c", "d"]
l3 = l1 + l2  # l3 -> ['a','b','c','d']

# ------ removing
l1 = []
l1.remove("Lundi")  # retire le premier 'Lundi' trouvé !! erreur sur aucun lundi !!
l1.clear()  # vide la liste complètement
l1.pop()  # remove last element on peut specifier un index ! erreur si l1 est vide
lettre = ["a", "b", "c", "d"].pop(2)  # lettre = 'c'  ! erreur si index mauvais
del l1[1]  # erreur si mauvais index


# ---- tester la présence en évitant les index "out of range"
if "a" in l1:
    pass

# ------ reverse
l1.reverse()  # l1 est modifié, aucun retour (None)
l2 = list(reversed(l1))  # liste renversé, l1 est inchangé

# ------ sort
liste = [1, 1, 4, 3, 3, 2, 6, 7, 7, 9, 2]
liste.sort()  # liste est modifiée
l2 = sorted(liste)  # liste N'est PAS modifiée !!

#  sort peut prendre plusieurs param : sort(*, key=None, reverse=False)

# ------ nested list
L1 = ["a", "b", "c", 1, 2, 3, ["apple", ["robert", "john"], "orange", "banana"]]
print(L1[6][1][0])  # robert
L1[6][1][0] = "Marylin"

# ---- index and count

# ---- iterating on list
list1 = [1, 5.30, True, None, "bonjour", "Francis"]
varBool = "Francis" in list1  # True
for item in list1:
    print(item)

# -------trier une liste de tuple avec un lambda
liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
liste.sort(key=lambda x: x[1])
print(liste)

# ------- autres méthodes
l2 = l1     # id(l1) = id(l2)
l2 = l1.copy()  # id(l1) = id(l2)
l1.

# ----------- intersection 2 listes
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
set(liste_01).intersection(set(liste_02))


# --- unpack
x = [1, 2, 3, 4]
print(*x)  # 1 2 3 4


# -------- remplacement dans une liste
liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
liste = [x.replace("Julie", "Julien") for x in liste]


# -------- min / max
x = min(["Pierre", "Marie", "Julie", "Adrien", "Julie"])  # Adrien
x = max([1000, -50, 0, -2, 100])  # 1000


# -----------  autres fonctions ----------------

# len       :   returns an int type specifying number of elements in the collection.
# min       :   Returns the smallest item from a collection.
# max       :   Returns the largest item in an iterable or the largest of two or more arguments.
# cmp       :   Compares two objects and returns an integer according to the outcome.
# sum       :   Returns a total of the items contained in the iterable object.
# sorted    :   Returns a sorted list from the iterable.
# reversed  :   Returns a reverse iterator over a sequence.
# all       :   Returns a Boolean value that indicates whether the collection contains only values that evaluate to True.
# any       :   Returns a Boolean value that indicates whether the collection contains any values that evaluate to True.
# enumerate :   Returns an enumerate object.
# zip       :   Returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
