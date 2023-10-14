# ----------------------------

#  --------------------------- DECORATOR -----------------------------

# Decorators are for functions, methods, or classes. Executed after and/or before decorated object
# used for : arguments validation/modification, modification of returned objects, e measurement of execution time, logging, thread synchro, caching, etc
# Decorator Stacking : @Outer -> @Inner -> function -> @Inner -> @Outer
# Class as a decorator : __init__ for self and the __call__ method, in which we call self.func()
# -> argument of decorator are passed in the __init__ method


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


# ------------------------------------ CLASS METHOD -----------------------------
# a class method requires 'cls' as the first parameter and a static method does not require self;
# a class method has the ability to access the state or methods of the class, and a static method does not;
# a class method is decorated by '@classmethod' and a static method by '@staticmethod';
# a class method can be used as an alternative way to create objects, and a static method is only a utility method.


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

# ------------------------------------  ABSTRACT CLASS   -----------------------------
# if any of the methods is an abstract one, then the class becomes abstract
# ABC : Abstract Base Classes
# all the abstract methods must be overwritten in the subclass (only 'pass' instruction is ok)
# TypeError if instanciating an abstract class
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

#  bp = BluePrint() # ---> TypeError: Can't instantiate abstract class BluePrint with abstract methods hello


# ------------------------------------  ENCAPSULATION  -----------------------------
# __var_name @property  @var_name.setter @var_name.delete
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

# ------------------------------------ COMPOSITION  -----------------------------
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

# ------------------------------------  Inheriting properties from built-in classes  -----------------------------
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
