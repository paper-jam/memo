# ================================= Metaprogramming ==================
# pylint: skip-file
# technique in which computer programs have the ability to modify their own or other programs’ codes


# ------------------------------------ metaclass -----
#  metaclass : a metaclass is a class whose instances are classes.
#  The typical use cases : logging/registering classes at creation time/interface checking/automatically adding new methods/variables.
#  the type of the metaclass type is type !
#  metaclasses are subclasses of the type class.
class Dog:
    pass


dog = Dog()
dog.__class__  # <class '__main__.Dog'> also = type(dog)
dog.__dict__  # {}

Dog.__name__  # Dog
Dog.__class__  # <class 'type'>
Dog.__bases__  # (<class 'object'>,)
Dog.__dict__  # {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Dog' objects>, '__weakref__': <attribute '__weakref__' of 'Dog' objects>, '__doc__': None}


# ------------------------------------ type function ----------------
# basic example
Dog2 = type("Dog", (), {})


# more complex example
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

# ------------------------------------  fin  -----------------------------
