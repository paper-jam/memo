# --================================  1 -- Advanced OOP ============================
# pylint: skip-file


# ------------------------- OOP fondations ----------------------------------
class Voiture:
    nb_roues = 4

    def rouler(self):
        pass


# le création d'une var. d'instance peu se faire dans une autre méthode que la méthode __init__
# elle peut aussi se faire directemnt par : (mais à eviter)
ma_voiture = Voiture()
ma_voiture.nouvelle_var_instance = 100

# pour une classe Voiture donnée :
Voiture.__class__  # ==> '<class Type>'
ma_voiture.__class__  # ==> '__main__.Voiture'
ma_voiture.rouler.__class__  # ==> <class 'method'>

# les var. d'instance sont stockée dans :
ma_voiture.__dict__

# les variables de classes sont stockés dans :
Voiture.__dict__

# La valeur d'une variable DOIT être modifié seulement en utilisant le nom de la classe !!
# et non pas le variable d'instance !
Voiture.nb_roues = 6

#  ----------------- OOP advanced -----------------------

# dunder : Le mot dunder est un raccourci de Double UNDERscore
# help() => documentation
# dir() => liste rapide sus forme d'une list()

# __iadd__, __add__, ... ne pas oublier : return self !
# heritance = MRO Method Resolution Order
# AttributeError :si appel d'une méthode inexistante
# when polymorphism is assumed, it is wise to handle exceptions that could pop up.

# args – refers to a tuple, *args collects all unmatched positional arguments;
# **kwargs (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs.
#  Likewise, **kwargs collects all unmatched keyword arguments.
# args and Kargs may be missing

#  ----------------- fin -----------------------
