# ----- =====================  formatting - f-string

# ---------- old format
print("%.2o" % (25))  # 31
print("%.5o" % (25))  # 00031


# ----------------- avec .format()
x = "{} {} {}".format("Geeks", "For", "Life")  # Geeks For Life
x = "{1} {0} {2}".format("Geeks", "For", "Life")
x = "{l} {f} {g}".format(g="Geeks", f="For", l="Life")
sentence = "the sum of {0} + {1} is {2}".format(10, 15, 25)  # format method

x = "{0:.2f}".format(40.509)  # '40.51'

# ----------------- avec f-string

# -------- f-string padding
lettre = "B"
symbol2 = "|"
size = 10
print(f"{symbol2}{lettre:^{size - 2}}{symbol2}")
# |     B     |

# -------- f-string  leading 0
cpt = 1
id_emp = f"id-{cpt:02}"  # --> id-01

# -------- f-string  numbers
x = 857922291304566146464
f"{x:E}"  # -> 8.579223e+20 (6 décimales)

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
