# -- ===== héritage

#  methode static : @staticmethod : la méthode peut être appelé sans instancié la classe

# voir l decorateur  @property

# un attribut de classe se declare normal comme une variable normale
# un attribut de classe est utilisé avec nomdeClasse.nomVar ou self.NomClasse


# ne pas oublier de passer self comme premier parma pour une méthode de base
# 'self' est une convention mais cela peut être remplacé par une autre string

# methode de classe avec le decorateur @classmethod, premier param cls
#  -> peut modifier une variable de classe cls.nomVarClasse = ...
#  -> doit être appelée directement depuis la classe Mois.nomClassMethod()
#  ->


# methode statique avec le decorateur @staticMethod, mais ce n'est pas obligatoire


#  -> pas de parametre cls ou self, maias des params standards
#  -> NE peut PAS modifier une variable de classe
#  -> doit être appelée directement depuis la classe Mois.nomStaticMethod()


# __init__ est appelée à la création
# __del__  est appelée à la desctruction
# __repr__ est appelé pour un lors d'un print
# __str__ est appelé pour un lors d'un str
# __methodePrivee(self):  avec un double underscore


# isinstance(var, Ma_classe) return true si var est une instance de Ma_classe,
# OU d'ue classe héritée de Ma_classe
class Test:
    A = 0

    def __init__(self):
        self.a = 0

    def une_fonction(self):
        self.a = 1


class Test2(Test):
    pass


# tester si sous-classe
x = Test2()
issubclass(Test2, Test)  # True
issubclass(x.__class__, Test)  # True


#  tester si une classe possède une variable de classe
hasattr(Test, "A")  # True
hasattr(Test, "a")  # False
hasattr(Test, "une_fonction")  # True


class Mois:
    # attribut de classe
    lieu_habitation = "Terre"

    # attribut de classe
    nb_de_mois_crees = 0

    def __init__(self, mois, annee):
        self.mois = mois
        self.annee = annee
        Mois.nb_de_mois_crees += 1

    def html_base(self):
        print("<h1>Voilà du code Html</h1>")

    # def __str__(self):
    #     return str(self.mois) + " -- str-- " + str(self.annee)

    # def __repr__(self):
    #     return f"{self.mois} {self.annee}"

    # Declaring private method with double underscore
    def __fun(self):
        print("Private method")

    #  destructeur
    def __del__(self):
        pass

    @classmethod
    def changer_planete(cls, nouvelle_planete):
        cls.lieu_habitation = nouvelle_planete

    @staticmethod
    def definition():
        print("l'humain est bête")


fev76 = Mois(2, 1976)
fev76.html_base()

# acces aux propriétés
print(f"L'annee est {fev76.annee} et le mois est {fev76.mois}")
print(fev76.__str__())
print(fev76.__repr__())


Mois.definition()

print(Mois.lieu_habitation)

Mois.changer_planete("Mars")
print(Mois.lieu_habitation)


# ------- méthode de classe qui permet de retourner une instance de classe
class Voiture(object):
    def __init__(self, marque):
        self.marque = marque

    @classmethod
    def lamborghini(cls):
        return cls("Lamborghini")


lamborghini = Voiture.lamborghini()


# ------------------ surcharge de la méthode __add__ avec héritage str
class Superstr(str):
    def __init__(self, a):
        self.a = a

    def __add__(self, chaine):
        return Superstr(f"{self.a} {chaine}")


print(Superstr("Bonjour") + "tout" + "le" + "monde")  # Bonjour tout le monde


# ----------------- autre exemple


# base class
class Vehicle:
    pays_vente_exclusive = "France"

    def __init__(self, color):
        self.color = color
        self.__px_vente = 100
        print(self.pays_vente_exclusive)
        # return self.color : NO !! -> TypeError a constructor returns always None

    def description(self):
        print("I'm a", self.color, "Vehicle")

    def affiche_px_vente(self):
        print(f"le prix de vente est {self.__px_vente}")

    def forget_self():
        print("method wher we forget self as argument")

    @staticmethod
    def identite():
        print("je suis une methode statique de la la classe Vehicle")

    @classmethod
    def changePays(cls, nouveau_pays):
        cls.pays_vente_exclusive = nouveau_pays


# subclass
class Car(Vehicle):
    def __init__(self, color, style):
        super().__init__(color)  # invoke Vehicle’s __init__() method
        self.style = style

    def description(self):
        print("I'm a", self.color, self.style)

    @classmethod
    def changePays(cls, nouveau_pays):
        cls.pays_vente_exclusive = nouveau_pays


# create an object from each class
v = Vehicle("Red")
c = Car("Black", "SUV")

# accessing a method declared without self argument
# v.forget_self() # TypeError: Vehicle.forget_self() takes 0 positional arguments but 1 was given


# accessing a private property
v1 = Vehicle("rouge")
v1.affiche_px_vente()  # OK
# print(f"le prix de vente est {v1.__px_vente}")  # ==> AttributeError


# inherit from two classe having the same method name
class TestA:
    def description(self):
        print("Je suis une méthode de la classe TestA")


class TestB:
    def description(self):
        print("Je suis une méthode de la classe TestB")


class TestC(TestA, TestB):
    def info(self):
        self.description()


C1 = TestC()
C1.description()  # "je suis ...TestA..." car Test1 est la premier argument ds la décalaration


v.description()
# Prints I'm a Red Vehicle
c.description()
# Prints I'm a Black SUV

# calling an inherited static method
Car.identite()

# calling an inherited class method
# Vehicle.changePays("Suède") OK
Car.changePays("Suède")


print(c.pays_vente_exclusive)


# inherit from two classe having the same variable name
class Parent:
    def __init__(self) -> None:
        self.age = 40

    def parent_get_age(self):
        print(self.age)


class Child(Parent):
    def __init__(self, p_age) -> None:
        self.age = p_age
        super().__init__()

    def child_get_age(self):
        print(self.age)


c1 = Child(10)
c1.child_get_age()  # !! le Child hérite de l'âge du parent !


# -- ============== objet and == operator
class Car:
    def __init__(self, x, y) -> None:
        self.name = x
        self.prix = y


c1 = Car("Audi", 5000)
c2 = Car("Audi", 5000)

print(c1 == c2)  # False ->  redefine __eq__ method for better result
