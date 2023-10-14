# ------ ====== EXCEPTIONS

#  ne pas confondre error et exception
#  Error : SyntaxError, TypeError, NameError, IndexError, KeyError, ZeroDivisionError, ImportError


#  --- syntax
try:
    ...
except ZeroDivisionError:
    ...
except Exception:
    ...
else:
    ...  # execute if no exception
finally:
    ...  # Some code .....always executed

# ----- nota

# un type d'exception traité 2 fois n'empêche pas l'éxecution de programme
# except ZeroDivisionError:
#   ...
# except ZeroDivisionError: ...
#     ...


#  ------------- exemple
try:
    #  attention  la variable myfile n'est pas accesible en dehors du bloc try
    with open(".\\test.txt", encoding="utf-8", mode="r") as myfile:
        premiere_ligne = myfile.readline()

    raise ValueError("Le fichier n'a pas été trouvé")  # pour lever une exception

except (FileNotFoundError, PermissionError) as e:     # if more than one execption type => parenthesis
    print("file does not exist")
    print(e.errno, e.strerror)
    print(e)

except Exception as e:  # except (without Eception) must be the last block
    print("there is another kind of error")
    print(e)
    raise Exception from e  # on peut relancer une exception avec l'exceptionn d'origine
else:
    print("clause else, all is OK")
    print(premiere_ligne)

finally:
    # it always run, Exception or not
    print("always run, exception or not")


# les exceptions à connaître
# ValueError : int('a), : valeur n’est pas correcte.
# TypeError : 1 + "a" : le type n'est pas correcte
# IndexError : "hello"[100] : index incorrect
# KeyError : d = {}, d['une cle'] : la clé n'existe pas ds le dictionnaire
# Autre : ZeroDivisionError, OSError , RuntimeError, SystemError, ModuleNotFoundError, NameError

# ------ ====== ASSERTIONS
import sys

assert "win32" in sys.platform, "This code runs on Windows only."
#  => raise an AssertionError on others platforms

print("windows OK")

# ------ ====== SYNTAX ERROR
# the program does not run and no exceptions are catched
# try:
#     print("Pytho"n")
# except:
#     print("error is raised")
# finally :
#     print("Code End")
# ==================> SyntaxError: unterminated string literal (detected at line 2)


--

