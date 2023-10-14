# ------============= SET

# les sets, séquence désordonnées d'éléments muables, hétérogènes, uniques
# pas d'accés par les index !! set[2] -> error
# surtout urtiliser pour des opérations ensemblistes

# ----- déclaration à  vide : ne pas utiliser {} car il s'agirait d'un dictionnaire
s1 = set()
S1 = set("bonjour")  # {'n', 'j', 'u', 'o', 'r', 'b'} (only one argument)
s1 = {"apple", "banana", "cherry"}
s1 = set(["papier", "ciseau", "papier"])  # from a list

# ----- doublons supprimés et éléments triés
s1 = {4, 2, 1, 8, 10, 3, 4, 10, 3}  # {1, 2, 3, 4, 8, 10}
s1 = {4, 2, 1, 8, 10, 3, "bonjour", 4, 10, 3, 2, 1, 5, "bonjour", "argent"}  # {1, 2, 3, 'bonjour', 4, 5, 8, 10, 'argent'}

# ---- no concat or multiply with operator
# {1}+{2} # TypeError !
# {1}*3  # TypeError !

# ---- removing duplictes


# ----- ajout
s1 = {1, 2, "pierre"}
s1.add(3)  # adding one element, and only ONE
s1.add((4, "pierre"))  # adding a tupple : {1, 2, 3, (4, 'pierre'), 'pierre'}
s1.add([5, "jean"])  # adding a liste ====> ne fonctionne pas !!!
s1.update([5, "jean"])  # {1, 2, 3, 'jean', 5, (4, 'pierre'), 'pierre'}

# ----- merging
s1 = {4, 5, 6}
s1.update({1, 2, 3, 4})  #  {1, 2, 3, 4, 5, 6} - accept list, string, tuples, set
s1.update([1, 2, 3, 4])  # {1, 2, 3, 4, 5, 6}

# ----- removing
# removing with remove or discard
s1 = {1, 2, 3, 4, 5, 6}
s1.remove(4)  # !! erreur si l'élément n'existe pas
s1.discard(4)  # pas d'erreur si l'élément n'existe pas
s1.pop()  # retire le PREMIER item, NO argument, méthode hasardeuse si le set n'est pas trié
s1.clear()  # dégage tout

# ------ tester la présence
if "pierre" in s1:
    pass

# Frozenset => les set deviens immuables
SET1 = frozenset(s1)  # Fset1.pop() # ---> erreur 'frozenset' object has no attribute 'pop'

# ------ operation ensembliste sur les sets
s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

s1.difference(s2)  # -> Python # retire les élemnts de s1 présenys dans s2
s1.difference_update(s2)  # compute and update s1 with the result

s1.intersection(s2)  # {'C++', 'Java'}   = s2.intersection(s1)
s1.difference_update(s2)  # compute and update s1 with the result

s1.symmetric_difference(s2)  # {'Python', 'C#'} = s2.symmetric_difference(s1)
# élements présents soit dans un set, soit dans l'autre, mais pas dans les deux. (XOR)
s1.symmetric_difference_update(s2)  # compute and update s1 with the result


s1.union(s2)  # {'C++', 'C#', 'Java', 'Python'} // pas de version _update
s1.isdisjoint(s2)  # False # True si aucuns éléments en commun
{"Python", "C++"}.issubset(s1)  # True / sous-ensemble
s1.issuperset({"Python", "C++"})  # True / surensemble
