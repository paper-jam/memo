# -- ===== ENUMERATES
capitales = ["Paris", "Milan", "New-York"]
for ville in enumerate(capitales, start=1):  # ville is a tuple # start optionnal
    print(ville)
# (1, 'Paris')
# (2, 'Milan')
# (3, 'New-York')


liste = ["Pierre", "Paul", "Marie"]
for i, prenom in enumerate(liste, start=1):
    print(i, prenom)


# ---- sur un dictionnaire
employees = {"mike": 27000, "anna": 15000, "john": 14000}

#  --- key and value
for i, (cle, valeur) in enumerate(employees.items(), start=1):
    print(i, cle, valeur)

#  --- value only
for i, valeur in enumerate(employees.values(), start=1):
    print(i, valeur)
