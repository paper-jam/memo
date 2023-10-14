# -- ========== les chaînes (IMMUTABLE)

# --  IMMUTABLE !
s1 = "Bonjour"
s1[0] = "b"  # TypeError: 'str' object does not support item assignment
s1.pop()  # AttributeError
s1 - "r"  # TypeError: unsupported operand
del s1[2]  # TypeError: 'str' object doesn't support item deletion

# -- les docs string
# https://peps.python.org/pep-0257/

# ----  les liste de string
# string.digits           0123456789

# string.ascii_letters    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_uppercase  ABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.ascii_lowercase  abcdefghijklmnopqrstuvwxyz

# string.printable          0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c
# string.punctuation        !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# -- attention à l'ordre ! les majuscules viennents AVANT les minuscules
# The ASCII code of m is greater than the ASCII code of M
print("mike" > "Mike")  # True
print(ord("m"))  # 109
print(ord("M"))  # 77


# -- == Strig on multiple lines with """
x = """Ces mille questions
Qui se ramifient
N'amènent, au fond,
Qu'ivresse et folie ;
"""

# -- pour info
x = """
"""
len(x)  # 1


# -- ===== Slicing
s1 = "abcdefghij"
s1[0]  # -> 'a' : premier  character
s1[-1]  # -> 'j' : dernier  character
s1[-2]  # -> 'i' : avant-dernier character
s1[4:10]  # 'efghij' 4 included, 10 excluded !
s1[:]  # 'abcdefghij'
s1[1:]  # 'bcdefghij' tout sauf le premier
s1[-4:]  # 'ghij' les 4 derniers
s1[0::2]  # 'acegi' 1 sur 2
len(s1)  # 10 int
s1[20]  # IndexError
s1[-2:-4]  # ''
s1[-2:-4:-1]  # 'ih' à rebrousse-poil, il faut un pas négatif

# -- ==== single quotes , double quote, line break, tab
x = '"Oui," disent-ils ! c\'est l\'arnaque complète, \nSomme perdue :\t\t 20000 € "'

x = "Peter's sister's name's \"Anna\""
x = "Peter's sister's name's \"Anna\""


# -- ===== Basic string methods
text = "monSieUr jEan-lUc dUpoNt"
text.upper()  # MONSIEUR JEAN-LUC DUPONT
text.lower()  # monsieur jean-luc dupont
text.capitalize()  # Monsieur jean-luc dupont

"xxxbonJOURyyy".title()  # XxxbonJOURyyy
"xxxbonJOURyyy".swapcase()  # XXXBONjourYYY
"++%?uûäéèàçoöôïî".swapcase()  # ++%?UÛÄÉÈÀÇOÖÔÏÎ
"xxxbonJOURyyy".removeprefix("xxx")  # bonJOURyyy
"xxxbonJOURyyy".removeprefix("xxx").removesuffix("yyy").title()  # Bonjour

"A9993".isdigit()  # False si NE contient QUE des chiffres de 0 à 9
"9993.00".isdigit()  # False !
"566616161146871314341".isdigit()  # true
"AAAAzzzzz9993Éöâ".isalnum()  # True, alphanumérique, y compris accent
"AAsfgsgfsdfsSdf".isalpha()  # True : que des char alpha
"uûäéèàÉçoöôïî".isalpha()  # les accentués sont bien pris en compte
"uûäéèàçoöôïî".isalpha()  # true

"++%?uûäéèàçoöôïî".islower()  # true
"uûäéèàÉçoöôïî".islower()  # False
"AABOJÉAZT".isupper()  # True
"+AABOJÉ-AZT:JJ".isupper()  # True

"Anatole".startswith("An")  # True, case sensitive
"Anatole".endswith("le")  # True, case sensitive


# -- ================== TRIM
x = "---" + "     bonjour    ".lstrip() + "---"  # ---bonjour    ---
x = "---" + "     bonjour    ".rstrip() + "---"  # '---     bonjour---
x = "---" + "     bonjour    ".strip() + "---"  # ---bonjour---

# -- ==== concat multiply
x = 3 * "bonjour " + "Monsieur"  #  'bonjour bonjour bonjour Monsieur'


# -- ==== spliting - split - par defaut " " est le séparateur
"ceci est un message".split()  # ['ceci', 'est', 'un', 'message']
"ceci est un message que j'aime bien lire".split(" ", maxsplit=2)  # ['ceci', 'est', "un message que j'aime bien lire"]

# -- ==== joining
" ".join(["ceci", "est", "un message que j'aime bien lire"])
#  =>  ceci est un message que j'aime bien lire

# -- ==== printing
# --- la fonction print permet de spécifier un séparateur et un terminateur
# ---  si terminateur, ne pas oublier le \n (terminateur par défaut)
print("Bonjour", "Monsieur", "Dupont", sep=" ", end=".\n")


# -- ==== finding counting
"je suis un gros mechant dinosaure".find("su")  # 3 -  str.find(sub[, start[, end]] )
"je suis un gros mechant dinosaure".rfind("e")  # 32 -  str.rfind(sub[, start[, end]] )

# ----- COUNT : STR LIST
# ----- compte le nombre d'occurence d'une chaîne, une liste ou tuple
code = "je cherche mon chemin"
code.count("ch")  # ---> 3
code.count("ch", 5)  # ---> 1
code.count("ch", 5, 10)  # ---> 2
# -- attention , sur les tuples : tuple.count() takes exactly one argument


# ----- replace
phrase = "Bonjour toi, Bonjour moi"
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir")  # 'Bonsoir toi, Bonsoir moi' / tts ls occurences
nouvelle_phrase = phrase.replace("Bonjour", "Bonsoir", 1)  # 'Bonsoir toi, Bonjour moi' / une seule occ.

# ------ convertir une phrase en camelCase
phrase = "Phrase en camel case"
p2 = phrase.lower().split()
res = p2[0] + "".join([x.title() for x in p2[1:]])


# ------ PRINT
print("09", "12", "2016", sep="-", end=" **\n")  # '09-12-2016 **' (ne pas oublier \n!)
print("Hello there!", end="")  # suppress newline
# with Python 2 --> sys.stdout.write("Hello there!")

# ------- ord / chr  :  code decimale Unicode du caractère
ord("A")  # int 65
chr(65)  # str A


# ----- =====================  formatting

# --- avec .format()
x = "{} {} {}".format("Geeks", "For", "Life")  # Geeks For Life
x = "{1} {0} {2}".format("Geeks", "For", "Life")
x = "{l} {f} {g}".format(g="Geeks", f="For", l="Life")
sentence = "the sum of {0} + {1} is {2}".format(10, 15, 25)  # format method

x = "{0:.2f}".format(40.509)  # '40.51'

# --- avec f-string

# -------- f-string padding
lettre = "B"
symbol2 = "|"
size = 10
print(f"{symbol2}{lettre:^{size - 2}}{symbol2}")
# |     B     |

# -------- f-string  leading 0
cpt = 1
id_emp = f"id-{cpt:02}"  # --> id-01


# --------- f-string
nombre = 2938.48872
decimales = 3
print(f"Nombre tronqué:{nombre : .{decimales}f}")


# use f Template class in the String module
from string import Template

Student = [("Ram", 90), ("Ankit", 78), ("Bob", 92)]
t = Template("Hi $name, you have got $marks marks")
for i in Student:
    print(t.substitute(name=i[0], marks=i[1]))
