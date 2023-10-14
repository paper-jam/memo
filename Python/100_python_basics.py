,# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304, expression-not-assigned, pointless-statement, line-too-long
# pylint: disable-next=unbalanced-tuple-unpacking
import math
import sys
import keyword

# Python is an interpreted language, which means the source code of a Python program is converted into bytecode (.pyc)
# that is then executed by the Python virtual machine (Python Virtual Machine)

# ---- all keyword :
keyword.kwlist
# 'False', 'None', 'True', 'and', 'as',
# 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# -- ======================== WRITING CODE

# -- shebang : placé sur 1ère ligne! pour os linux-Mac, aucun effet sur Windows, sauf wsl
# -- allow to execute a runnable scripts without explicitly specifying the program
#!/usr/bin/python3

# --  comment on one line
""" how to
comment on
multi lines """

# -- multiple instructions one line
# t = "bon" ; v = "jour" ; print(t + v)  # bonjour

# cut line
if True:
    t = "je suis un gros \
mutant"  # no indent !


# ------- FOR -- while
# le code du ELSE n'est pas executé sur un break
x = 8
while x < 10 and x >= 0:  # dès que cette condition ne sera plus vérifiée, le code du else sera exécuté
    print(x)
    x -= 1
    if x == 5:
        break  # le code du else ne sera pas exécuté
else:
    print("x is not less than 10")

for i in range(50):
    print(i)
    if i == 40:
        break  # le code du eslse ne sera pas exécuté
else:
    print("finito !")

# ----- if
if 90 <= x <= 100 : # syntax OK
    pass





# ------ iterate on a string
for i in "abcde":
    print(i)

# ------- switch -- depuis python 3.10
lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")

# ------------ ------------ ---------------- ------------------ -------------------- ------------ ---------


# -------- parsing and running python code with eval
x = 1
variable = "x+1"
var2 = eval(variable)  # var2 = 2
eval("138")  #  => 138 as int
eval("138.0")  #  => 138 as float
eval("138.0+10")  #  => 148 as float
eval("'10'*a")  #  => 148 as float
eval("'a'*10")  #


# -------- min / max
min_value = min(1, 2, 3)
max_value = max(1, 2, 3)




# -- ============== arguments of the command line
print(sys.argv[0])  # fisrt agument = name of the program
print(sys.argv[1])  # second argument
print(sys.argv[2])  # third argument
argument_list = sys.argv[1:]
for arg in argument_list:
    print(arg)

# ********** input plusieurs valeurs
x, y = input("Enter two values: ").split()


# -- ====================================== LIST, TUPLES, SET, DICTIONARIES ============

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered**(since python 3.7) and changeable. No items with the same key.

# -- LIST -- voir fichier
# -- TUPLE -- idem
# -- DICT -- -- idem

# -- ====================================== comparison operators ============


# -- ===== accepting user input
inputValue = input(
    "enter your value : ",
)
if inputValue.isdigit():
    print("your number  is : " + str(int(inputValue.strip())))
else:
    print("your string  is : " + inputValue.strip())


# -- =====
if __name__ == "__main__":
    pass





# -- =====  Threading
# import threading
# t = threading.Thread(target=maFonction, args=[unParametre])
# t.start()
# t.join()


# -- =====  VSCODE debugging
# if __name__ == '__main__':
#     app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
