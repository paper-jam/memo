# -- ========================= VARIABLES

#   Python is case sensitive

# -- basics on type : 4 basics type : int, str, bool, float, complex
#   - python has no command for declaring a variable.
#   - a variable is created the moment you first assign a value to it.

# -- naming conventions,  Pep8 , for variables
#    only letters (case matters !), numbers or underscore, can't start with a number
#    for variables : lowercase with underscore : my_var
#    const in uppercase

# -- Reassign changes id, if value or type changes
x = "Bonjour"  # id(x) -> 2406103052848
x = "Bonsoir"  # id(x) -> 2406103053104
y = x[:]  # id(y) -> 2406103053104  id(y) = id(x) !
val_bool = y is x  # True, and also True for
# --> is : same memory location so same value

# -- use rather isinstance(var, str) than type(var) == 'str'
isinstance(28.0, int)  # False
type(28.0)  # <class 'float'>

# --  ckecking var name is a keyword (needs import keyword)
keyword.iskeyword("def")
keyword.kwlist
# and = 3 # ==> SyntaxError: invalid syntax
# import math; math = 3 # => strange but OK


# -- scientific notation with 'e' ('E' works OK but 'e' is better)
x = 2e8  #  200000000.0 (float)
# 1.23E-7 == 1.23e-7 == 1.23*10**-7

# -- int and float function
int = 01  # erroe
int("320.00")  # ValueError
int(320.99)  # 320
int(True)  # 1
int(False)  # 0


float("320.02")  # OK : param is str, int, float or bool
float(True)  # 1.0
float(False)  # 0.0

# binary 0b, octal 0o, hexadecimal 0x
val_bin = 0b001010  # int(val_bin) -> 10
val_oct = 0o756212  # int(val_oct) -> 253066
val_hex = 0x0FDAB5  # int(val_hex) -> 1039029

# binary,octal,hexadecimal -> are not TYPEs !
type(val_bin)  # <class 'int'>
type(val_oct)  # <class 'int'>
type(val_hex)  # <class 'int'>

# conversion bin/oct/hex
val_dec = 156319
bin(val_dec)  # 0b100110001010011111
oct(val_dec)  # 0o461237
hex(val_dec)  # '0x2629f'

# conversion int from hex or oct
int("2629f", 16)  # 156319
int("461237", 8)  # 156319
int("100110001010011111", 2)  # 156319
int("0o461237")  # ==> error

# conversion bin to dec
int("100", 2)  # 4
int("0b100", 2)  # 4


# -- ========================= OPERATOR ========================================


# = affectation, mutiple affectation, swapping
x = y = z = 1  # x=1 y=1 z=1
x, y = 15, 20  # x = 15 , y = 20
x, y = y, x  # x = 20 , y = 15  # --> swapping !

# unary operators, needs only one operator :  + - ~ not


# increment : first operator, then =
x = 1
x += 1  # 2
x *= 2  # 4
x **= 2  # 16
x -= 1  # 15
x %= 7  # 1
x = 7
x //= 3  # 2 (floor division) => float

# floor division renvoi un int


# -- opérateurs autres que +-/*
x = 5 % 2  # 1 -> modulo restant de la division
x = 2**3**3  # 512 !! attention au piège
x = 5 // 2  # 2 -> partie entière de la division

# -- remarques exposant : 3 solutions
x = 2**3
x = pow(2, 3)
x = math.pow(2, 3)

# -- string operators: * +
x = "bon" + "jour"  # 'bonjour'
y = x * 3  # 'bonjourbonjourbonjour'

# -- bitwise operators: ~ & ^ | << >>
x = ~1  # -2 - inversion des bits
x = 255 & 0  # 0 - AND bit par bit
x = 255 | 0  # 255 - OR bit par bit
x = 255 ^ 0  # 255 - XOR bit par bit
x = 10 << 1  # 20 / decalage à gauche -> 00001010 ---> 00010100 / multiply par 2
x = 10 << 2  # 40 / 00001010 ---> 00101000 , / multiply par 2
x = 10 >> 1  # 5  / decalage à droite : 00001010 ---> 00000101 / division par 2 avec arr.
x = 1 >> 1  # 0

# -- qq exemples
x = 1234567890 ^ 1234567890  # x = 0

# -- priority
# 1  ** (de droite à gauche) # 2**2**3 = 256 ## 2**3**2 = 512

# 2 +w -x ~x

# 3  * / // % (priorité gauche à droite 5//4*3 -> 3 tandis que  5*4//3 -> 6 )
# 4  + -

# -- les bitwise
# 5 << >>
# 6 & and
# 7 ^ xor
# 8 | or

# bool
# 9 == != <= <> < > is not
# 10 not
# 11 and
# 12 or

# -- logical operator
# < <= > >= == != and  or not
print("bonjour" > "bon")  # True ( comme ds le dico


# -- bitwise operator
# &     AND     Sets each bit to 1 if both bits are 1
# |     OR      Sets each bit to 1 if one of two bits is 1
# ^     XOR     Sets each bit to 1 if only one of two bits is 1
# ~     NOT     Inverts all the bits
# <<    Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>    Signed right shift  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


# -- ===================  valeur booléennes (and, or , not)
# What is False : 0 and empty collections : [] {} ()

# ---- attention à None
# None == False  # -> False
# None == True   # -> False
# => None n'est ni True ni False
# if var == None ... -> à éviter, préférer if var is None ...
# None + None # => TypeError
# None + 1 # => TypeError
# None = None # True
# None != None # False
# None = None # true
# None >= None # TypeError
# None > None # TypeError

# -- permet de savoir si a a bien une valeur
a = 0
if a is not None:
    print(a)

# --- concatenation with other type
x = False + True  # 1
x = False + 1  # 1
x = True + 1  # 2
x = True + 1.0  # 2.0
# x = True + 'a' ==> TypeError
l1 = [False, True, "2", 3, 4, 5]
0 in l1  # True !! The 'in' operator uses the equal to operator on every element of the list.


# ---- here are some comparisons
x = 10 == 10  # true
x = "hello" == "Hello"  # false
x = 10 == 10.00  # true

# > >= < <= != (not equal)

# AND operations are performed first from left to right
# then the OR operations are performed
print(False or True and False)  # False
print(not False)  # not -> opposite


# -- =================== are variables equals ?
# is : same memory location
# == : same value
# int / str / bool :  variables with the same value have the same id
# float            :  variables with the same value DOES NOT have the same id
# list             :

x = 3
y = 3
print(x == y)  # true

# --------------- control flow
# ------ bloc de code : si une seule ligne de code pour un bloc, possibilité d'aligner

if 1 > 0:
    print("OK")
for x in range(4):
    print("OK")

# ------- IF
if 5 < 6:
    print("one")
elif 5 < 6:
    print("one")
else:
    pass  # pass : does nothing but compile correctly
# le else à la fin, n'est pas obligatoire


# -------- opérateur ternaire : [on_true] if [expression] else [on_false]
age = 20
print("majeur") if age >= 18 else print("mineur")
