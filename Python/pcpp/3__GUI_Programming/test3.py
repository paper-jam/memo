class Meta(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class.instances = 0
        original_init = new_class.__init__

        def new_init(self, *args, **kwargs):
            new_class.instances += 1
            original_init(self, *args, **kwargs)

        new_class.__init__ = new_init
        return new_class


class MyClass(metaclass=Meta):
    pass


a = MyClass()
b = MyClass()
c = MyClass()


print(MyClass.instances)
