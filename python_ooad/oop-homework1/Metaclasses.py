class MyMeta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"Creating class: {name}")
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

class YourClass(metaclass=MyMeta):
    pass

obj = MyClass()
obj2 = YourClass()