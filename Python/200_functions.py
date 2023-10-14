# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
import keyword
import math

#  ---------------=========================  fonctions
# -------- attention : les arguments obligatoires sont déclarés en premier ::
# def multiplicateur_mot(mult=5, mot):  ---> # ---> SyntaxError: non-default argument follows default argument !!!

# ----- getting help on a function
help(print)


# ---- evaluation parameter : from left to right
def show(x):
    print(x, end="")
    return 0


print(show(1) & show(2) + show(3) * show(4) ** show(5))

# 123450

# passage de parame par reference selon qu'ils sont mutables ou pas
# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747
# une liste passée en argument d'une fionction et qui modifié dans le corps de la fonction, prvoque le modifcation de l'argument
# à tester


# ---- basics  declaring , calling
# d'abord les arguments par position, ensuite les arguments nommés !
def func1(child1, child2):
    print("The youngest child is " + child2)


# my_function(child1="Emil") # missing 1 required positional argument: 'child2'
func1("Emil", child2="Tobias")  # OK


# ---- param optionnels
def f2(child1, child2="bob"):
    print("The childs are " + child1 + " and " + child2)


f2("Emil")  # OK


# ----- SORT
# paramètre optionnel :clé de tri
utilisateurs = [("user1", "Etienne"), ("user2", "Paul")]
utilisateurs.sort(key=lambda x: x[1])  # --> tri sur le prénom


def greet_person(name="francis"):
    print("bonjour " + str(name))


#  function with default value # arg is a tuple
def my_sum(*arg):
    print(sum(arg))


my_sum(1, 2, 100, 300)  # 403


# ------- PACKING UNPACKING ----------
# we can use Packing to pack all arguments in a tuple.
# *args stands for positional arguments, for iterables
# and kwargs in **kwargs stands for keyword arguments, for dict


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)


add_numbers(1, 2, 3)  # OK
add_numbers(*[10, 20, 30])  # OK !!
t1 = (10, 20, 30)
add_numbers(t1)  # erreur
add_numbers(*t1)  # OK !


# kwarg is a dict
def f1(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["grand"])


f1(name="Francis", poids=92, grand=True)


# ------ DIR()
# The dir() method returns the list of valid attributes of the passed object.


# ------ EVAL
# Eval parse a string and evaluate it as a python expression
i = input("calc : ")  # 44+5
eval(i)  # -> 49

# -- ====== max, min
max([1, 2, 3, 4, 5, 6])  # 6
min([1, 2, 3, 4, 5, 6])  # 1
min(["Paris", "Milan", "New-York"])  # Milan
max(["Paris", "Milan", "New-York"])  # Paris


# --  attribuer une variable à une fonction
def shout(text):
    return text.upper()


yell = shout
yell("bonnjour")  # -> BONJOUR


# -- =========================== fonctions diverses

# ------ The any() function returns True if any element of an iterable is True
l1 = ["True", "False", 0]
any(l1)  # --->  True
any([])  # --->  False
any([1])  # ---> True
any([0])  # ---> False


# ------ The all() function returns True if all elements of an iterable are True
l1 = ["True", 1, ["Pierre"]]
all(l1)  # --->  True
all([])  # --->  True ! Empty iterable ==> true !!
all([1])  # ---> True
all([0])  # ---> False


# -- ===== range
demoRange = range(20, 30, 2)  # start, stop, increment (stop value excludesd
for n in demoRange:
    print(n, end=" ")

range(0, 10, 0)  # ValueError: range() arg 3 must not be zero !

list(range(0))  # []
list(range(1))  # [0]
list(range(2))  # [0, 1]
list(range(0, 0))  # []
list(range(1, 1))  # []
list(range(1, 10, -1))  # []

# ---- in a range, index is a local value ...
i = 0
for i in range(0, 4):
    print(i, end=" ")
    i = i + 10  # ... hence it has no impact
else:
    print("Python")
# ==> 0 1 2 3 Python


# -------- simplifier :  rangerange(0,11) ---> range(11)
for idx in range(11):
    pass

# ---- la fonction range admet un argument qui permet d'établir rapidement une liste de nombres pairs
liste_nombre_pairs = range(2, 101, 2)
list(liste_nombre_pairs)
