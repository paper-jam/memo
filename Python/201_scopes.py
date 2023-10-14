#  ---------------=========================  Scopes

#  une variable déclarée avec le même nom qu'une variable globale prend le pas
# sans changer la valeur de la var. globale

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)


# le mot clé global permet de rendre globale une variable, au sein d'une fonction
# à la déclaration avec 'global', elle reprend la valeur précédemment définie


# mais attention :
def sum(x):
    global x  # ===> SyntaxError: name 'x' is parameter and global
