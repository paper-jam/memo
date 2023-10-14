# --================================  1 -- Advanced OOP ============================
# pylint: skip-file

# ================ module 1 - OOP fondations ====================
class Voiture:
    nb_roues = 4

    def rouler(self):
        pass


# le création d'une var. d'instance peu se faire dans une autre méthode que la méthode __init__
# elle peut aussi se faire directement par : (mais à eviter)
ma_voiture = Voiture()
ma_voiture.nouvelle_var_instance = 100

# pour une classe Voiture donnée :
Voiture.__class__  # ==> '<class Type>'
Voiture.__name__  # ==> 'Voiture'
Voiture.__bases__  # (tuple avec la liste des classes héritées implicitement ou sinon 'object')
Voiture.__mro__  # (tuple avec la liste des classes héritées + object + la classe elle-même)


ma_voiture.__class__  # ==> '__main__.Voiture'
ma_voiture.__name__  # ==> AttributeError
ma_voiture.rouler.__class__  # ==> <class 'method'>

# les var. d'instance sont stockée dans :
ma_voiture.__dict__

# les variables de classes sont stockés dans :
Voiture.__dict__


# La valeur d'une variable de class doit être modifié SEULEMENT en utilisant le nom de la classe !!
# et non pas le variable d'instance ! sinon , il y aura création d'une variable d'instance
Voiture.nb_roues = 6


#  ----------------- OOP advanced -----------------------

# dunder : Le mot dunder est un raccourci de Double UNDERscore

# __variable    : private variable, inaccessible depuis l'exterieure ou les classes descendantes
# __var         : protected variable, par convention reste accessible depuis extérieure

# dir(Voiture) => list of the attributes and methods of the object
# help(Voiure) => detailed documentation on the parameter



# redefining the + operator with the add method
class Person:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30)
p2 = Person(35)

print(p1 + p2)  # 65

# ================ module 2 - OOP advanced  =====================================

# ----- Inheritance - MRO
# heritance = MRO Method Resolution Order, considère l'ordre des classes héritées
class D(B, C):
    pass

D().info() # -> recherche la méthode .info() dans la classe B, puis dans la classe C

# si héritage complexe et que le MRO échoue -> Type Error
TypeError: Cannot create a consistent method resolution, order (MRO) for bases A, C

# ----- Polymorphism

# ------ duck Typing
# AttributeError :si appel d'une méthode inexistante
# when polymorphism is assumed, it is wise to handle exceptions that could pop up.


# ------ Extended function argument syntax
# *args – refers to a tuple, *args collects all unmatched positional arguments;
# **kwargs (keyword arguments) – refers to a dictionary of all unexpected arguments that were passed in the form of keyword=value pairs.
# args and Kargs may be missing

def combiner(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))

    # way to call another function passing arg and kwargs, still with asterix
    other_function(*args, **kwargs)

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')

# 10 <class 'int'>
# 20 <class 'str'>
# (40, 60, 30) <class 'tuple'>
# {'argument1': 50, 'argument2': '66'} <class 'dict'>

#  ---------------- DECORATOR ----------------

# Decorators are for  : functions, methods, or classes.
# Executed after and/or before decorated object
# used for :
# - the validation of arguments;
# - the modification of arguments;
# - the modification of returned objects;
# - the measurement of execution time;
# - message logging;
# - thread synchronization;
# - code refactorization;
# - caching


# Decorator Stacking : @Outer -> @Inner -> function -> @Inner -> @Outer
# Class as a decorator : __init__ for self and the __call__ method, in which we call self.func()
# -> argument of decorator are passed in the __init__ method

# -- Decorators can accept their own attributes
def warehouse_decorator(material):
    def wrapper(our_function):
        def internal_wrapper(*args):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, material))
            our_function(*args)
            print()
        return internal_wrapper
    return wrapper


@warehouse_decorator('kraft')
def pack_books(*args):
    print("We'll pack books:", args)


@warehouse_decorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@warehouse_decorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')


# ---- Decorating functions with classes
class SimpleDecorator:
    def __init__(self, own_function):
        self.func = own_function

    def __call__(self, *args, **kwargs):
        print('"{}" was called with the following arguments'.format(self.func.__name__))
        print('\t{}\n\t{}\n'.format(args, kwargs))
        self.func(*args, **kwargs)
        print('Decorator is still operating')

@SimpleDecorator
def combiner(*args, **kwargs):
    print("\tHello from the decorated function; received arguments:", args, kwargs)

combiner('a', 'b', exec='yes')




#   this line defines a decorating function that accepts one parameter 'class_'
def object_counter(class_):
    # copy of the reference to the __getattribute__ special method.
    class_.__getattr__orig = class_.__getattribute__

    # du coup, on definit une nouvelle méthode d'accès aux attributs
    def new_getattr(self, name):
        if name == "mileage":
            print("We noticed that the mileage attribute was read")

        # on retourne ce qui est demandé à la base
        return class_.__getattr__orig(self, name)

    # on affecte la nouvelle méthode, à so nom originel
    class_.__getattribute__ = new_getattr
    return class_


@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN


car = Car("ABC123")
print("The mileage is", car.mileage)
print("The VIN is", car.VIN)


# ---------------- CLASS METHOD ----------------
# a class method requires 'cls' as the first parameter and a static method does not require self;
# a class method has the ability to access the state or methods of the class, and a static method does not;
# a class method is decorated by '@classmethod' and a static method by '@staticmethod';
# a class method can be used as an alternative way to create objects, and a static method is only a utility method.
# a class method works on the class itself
class Car2:
    def __init__(self, vin):
        print("Ordinary __init__ was called for", vin)
        self.vin = vin
        self.brand = ""

    # permet la création d'une instance de classe Car
    @classmethod
    def including_brand(cls, vin, brand):
        print("Class method was called")
        _car = cls(vin)
        _car.brand = brand
        return _car  # permet la création d'une instance de classe Car


car1 = Car2("ABCD1234")
car2 = Car2.including_brand("DEF567", "NewBrand")

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)

# ---------------- STATIC METHOD ----------------
# does not require cls as the first parameter
# cannot access the state or methods of the class
# is only a utility method
class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


# ----------------  ABSTRACT CLASS   ----------------
# abstract class must inherit from abc.ABC (Abstract Base Classes)
# if any of the methods is an abstract one, then the class becomes abstract
# all the abstract methods must be overwritten in the subclass (only 'pass' instruction is ok)
# TypeError if instanciating an abstract class
# TypeError if instanciating a subclass where abstrcat method has not been implemented
import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print("Welcome to Green Field!")

gf = GreenField()
gf.hello()

bp = BluePrint() # ---> TypeError: Can't instantiate abstract class BluePrint with abstract methods hello


# ----------------  ENCAPSULATION  ----------------
# __var_name /  @property /  @var_name.setter / @var_name.deleter
# .setter et .deleter  sont optionels mais erreur s'ils sont appelés
class Tank:
    def __init__(self, capacity):
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, new_level):
        self.__level = new_level

    @level.deleter
    def level(self):
        self.__level = None
        print("deleter is used")


# initiate, change, and delete
our_tank = Tank(20)
our_tank.level = 10
del our_tank.level

# ---------------- COMPOSITION  ----------------
#  composition transfers additional responsibilities to the developer
# Composition is a "has a" solution while inheritance is a "is a" relation


class Car:
    def __init__(self, engine):
        self.engine = engine


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print("Starting {}hp gas engine".format(self.hp))


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print("Starting {}hp diesel engine".format(self.hp))


my_car = Car(GasEngine(4))
my_car.engine.start()
my_car.engine = DieselEngine(2)
my_car.engine.start()

# ----------------  Inheriting properties from built-in classes  ----------------
#  built-in dictionary,  equipped with logging mechanism, for writing and reading operations performed
from datetime import datetime


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp("MonitoredDict created")

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp("value for key [{}] retrieved".format(key))
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp("value for key [{}] set".format(key))

    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append("{} {}".format(timestampStr, message))


kk = MonitoredDict()
kk[10] = 15
kk[20] = 5

print("Element kk[10]:", kk[10])
print("Whole dictionary:", kk)
print("Our log book:")
print("".join(kk.log))


# ================ module 3 - advanced techniques exceptions ====================

#   ---------------- UnicodeError ----------------
try:
    b"\x80".decode("utf-8")
except UnicodeError as e:
    print(e)  # 'utf-8' codec can't decode byte 0x80 in position 0: invalid start byte
    print(e.encoding)  # utf-8 -- the name of the encoding that raised the error.
    print(e.reason)  # invalid start byte -- a string describing the specific codec error.
    print(e.object)  # b'\x80' --  the object the codec was attempting to encode or decode
    print(e.start)  # 0 -- the first index of invalid data in the object
    print(e.end)  # 1 -- the index after the last invalid data in the object


# ----------------  chained exception  ----------------
# the __context__ attribute, for implicitly chained exceptions; -
#   implicite : qui est levée alors que le traitement d'une exception précédente était déja en cours
# the __cause__ attribute,  for explicitly chained exceptions.
#   explicite : translating an exception for unifying behavior of exception handling

# ----------------  exception implicite  ----------------
a_list = ["First error", "Second error"]

try:
    print(a_list[3])
except Exception as e:
    try:
        # the following line is a developer mistake - they wanted to print progress as 1/10 but wrote 1/0
        print(1 / 0)
    except ZeroDivisionError as f:
        print("Inner exception (f):", f)
        print("Outer exception (e):", e)
        print("Outer exception referenced:", f.__context__)
        print("Is it the same object:", f.__context__ is e)  # True : f.__context__ = e


# ----------------  exception explicite  ----------------
class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError("Crew is incomplete") from e


def fuel_check():
    try:
        print("Fuel tank is full in {}%".format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Problem with fuel gauge") from e


crew = ["John", "Mary", "Mike"]
fuel = 100
check_list = [personnel_check, fuel_check]

print("Final check procedure")

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))

#  ===> explicity chaining with "raise" f.__cause__ = e


# ----------------  traceback  ----------------
import traceback

try:
    x = 100 / 0

except Exception as f:
    print(f.__traceback__)  #   <traceback object at 0x7f3b06928b40>
    print(type(f.__traceback__))  # <class 'traceback'>

    details = traceback.format_tb(f.__traceback__)
    print("".join(details))


# ================ module 4 - objects persistence ====================

# ------------------------------------ id shallow and deep copy -----
# id() is is the address of the object in the memory
# avoid naming a variable as id
# a shallow copy is only one level deep
# deep copy might cause problems when there are cyclic references in the structure to be copied
# a deep copy operation takes significantly more time than any shallow copy operation;
import copy

l1 = ["a", [1, 2, 3]]
shallow_copy_list = copy.copy(l1)
deep_copy_list = copy.deepcopy(l1)

# a deep copy is really deep
l1 = [1, 2, ["Arthur", "Bob", {"pays": ["France", "Italie"]}]]
l2 = copy.deepcopy(l1)
l2[2][2]["pays"][1] = "Belgique"
# l1 ==> [1, 2, ['Arthur', 'Bob', {'pays': ['France', 'Italie']}]]
# l2 ==> [1, 2, ['Arthur', 'Bob', {'pays': ['France', 'Belgique']}]]

# nota : making a true copy of a list
b_list = a_list[:]


# pour rappel
# == This operator compares the values of both operands and checks for value equality.



# ------------------------------------ Serialization with pickle ----------------
# types that can be pickled
#  - None
#  - boolean
#  - integer
#  - floating-point
#  - complex
#  - strings bytes
#  - bytearrays
#  - tuples, lists, sets, and dictionaries containing pickleable objects
#  - objects, including objects with references to other objects (remember to avoid cycles!)
#  - references to functions and classes, but not their definitions.

# main method are : import pickle, pickle.dump(), pickle.load()
# for serialized object : pickle.dumps() and pickle.loads()
# the order in which the objects were persisted (dump)
# and the deserialization (.load) code should follow the same order.

# non-pickleable objects will raise the PicklingError exception
# pickling a function or class, pickles only the name, not the code
# avoid pickling highly recursive data structure -> 'RecursionError'
# 'AttributeError' if function/class code in missing when reading the pickle file

# picke module is a Python implementation, not compatible with Java/C++ .. => use JSON or XML
# use the same version of pickel for serializing and deserializing !
# pickel is not secure : care !

import pickle

a_list = ["a", 123, [10, 100, 1000]]
bytes = pickle.dumps(a_list)
print("Intermediate object type, used to preserve data:", type(bytes))

# now pass 'bytes' to appropriate driver

# therefore when you receive a bytes object from an appropriate driver you can deserialize it
b_list = pickle.loads(bytes)
print("A type of deserialized object:", type(b_list))
print("Contents:", b_list)


# ------------------------------------ Serialization with shelve-----
# objects are pickled and associated with a key. The keys must be ordinary strings.
# then the order in which objects are serialized no more matters

# 'r'   Open existing database for reading only
# 'w'   Open existing database for reading and writing
# 'c'   Open database for reading and writing, creating it if it doesn’t exist (this is a default value)
# 'n'   Always create a new, empty database, open for reading and writing

# sync() or close() flush the buffers
# shelve is a dict, so we can use : len(), in, keys(), items(), update(), del()
# shelve is no more secure than pickle

import shelve

shelve_name = "first_shelve.shlv"

my_shelve = shelve.open(shelve_name, flag="c")
my_shelve["EUR"] = {"code": "Euro", "symbol": "€"}
my_shelve["GBP"] = {"code": "Pounds sterling", "symbol": "£"}
my_shelve["USD"] = {"code": "US dollar", "symbol": "$"}
my_shelve["JPY"] = {"code": "Japanese yen", "symbol": "¥"}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve["USD"])
new_shelve.close()


# ================ module 5 - metaprogramming  ====================
# technique in which computer programs have the ability to modify their own or other programs’ codes


# ------------------------------------ metaclass -----
#  metaclass : a metaclass is a class whose instances are classes.
#  The typical use cases :
#  - logging
#  - registering classes at creation time
#  - interface checking
#  - automatically adding new methods
#  - automatically adding new variables.
#  the type of the metaclass type is type !
#  metaclasses are subclasses of the type class.
class Dog:
    pass



# ------------------------------------ type function ----------------
# When the type() function is called with 3 arguments, dynamically creates a new class.
# type(, , )
# - name of the class
# - inherited classes (will be returned by __bases__)
# - dictionary containing method definitions and variables for the class body



# ----------------- example 1
def bark(self):
    print('Woof, woof')

class Animal:
    def feed(self):
        print('It is feeding time!')

Dog = type('Dog', (Animal, ), {'age':0, 'bark':bark})

print('The class name is:', Dog.__name__)
print('The class is an instance of:', Dog.__class__)
print('The class is based on:', Dog.__bases__)
print('The class attributes are:', Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()


# ------------------ more complex example
def greetings(self):
    print("Just a greeting function, but it could be something more serious like a check sum")


class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if "greetings" not in dictionary:
            dictionary["greetings"] = greetings
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj


class My_Class1(metaclass=My_Meta):
    pass


class My_Class2(metaclass=My_Meta):
    def greetings(self):
        print("We are ready to greet you!")


myobj1 = My_Class1()
myobj1.greetings()
myobj2 = My_Class2()
myobj2.greetings()

# ------------------------- FIN ------------------
