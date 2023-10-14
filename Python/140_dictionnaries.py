# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
# ---- dictionnaries

# Dictionary is a collection which is ordered**(since python 3.7) and changeable. No members with the same key.

# --- ==== declaration
d1 = {}
d2 = dict()
poids = {"francis": 91, "bob": 55, "anna": 31}

# --- ==== adding
poids["cath"] = 66  # adding a element
poids.items()
p2 = {"jean": 100}
# p3 = poids + p2 does not work !! error -> use .update()

# --- ==== accessing
poids.get("cath")  # None if inexisting key
poids["cath"]  # error if inexisting key !!
poids.keys()  # dict_keys(['francis', 'bob', 'anna', 'cath'])
poids.values()  # dict_values([91, 55, 31, 66]) -> iterable
poids.items()  # dict_items([('francis', 91), ('bob', 55), ('anna', 31)])

# --- ==== removing
poids_bob = poids.pop("bob")  # removing by key, error if inexisting key !
x = poids.popitem()  # ->Tuple - remove the last (LIFO) element since Python 3.7
poids.clear()

# --- ==== testing presence ...
x = "francis" in poids.keys()  # .. of a key
x = 55 in poids.values()  # .. of a value

# --- ==== casting to list
l = list(poids)  # ==> ce sont les keys qui sont prises en comptes, pas les "values" !!
l1 = list(poids.keys())
l2 = list(poids.values())

# --- ==== autres fonctions
len(poids)  # nb elements

# -- ===== iterating on dictionnaries, with unpacking
employees = {"mike": 27000, "anna": 15000, "john": 14000}

for entry in employees.items():
    print(entry)  # entry is a tuple

for salary in employees.values():
    print(salary)

for firstName in employees.keys():
    print(firstName)

for key, value in employees.items():
    print(key + "--->" + str(value))


# -- ====== check if value is in a dic
print(140 in {"john": 140}.values())  # True


# -- ====== combining dictionnaries

# -- merge method with d1.update(d2) - d2 values have priority
dict_1 = {"John": 15, "Rick": 10, "Misa": 12}
dict_2 = {"Bonnie": 18, "Rick": 20, "Matt": 16}
dict_1.update(dict_2)  # {"John": 15, "Rick": 20, "Misa": 12, "Bonnie": 18, "Matt": 16}


# -- merge method with "|" since Python 3.9
d1 = {"a": 1, "b": 2}
d2 = {"b": None, "c": 3, "d": 4}
d3 = {"e": 5, "f": 6}

combined = d1 | d2 | d3


# ---- nota
# a tuple can be a key of a dictonnary
d = {("A", "B"): "bonjour"}

# ---- an tuple can be an index of a dictionnary
x = {(1, 2): 1, (2, 3): 2}
print(x[1, 2])

# ---- a dictionnary can have a float or integer as a key, but...
d = {1: "Bonjour"}
d[1.0] = "Bonsoir"  # => remplace la key
d[1.00000001] = "A bientôt"
# d => {1: 'Bonsoir', 1.00000001: 'Bonsoir'}
