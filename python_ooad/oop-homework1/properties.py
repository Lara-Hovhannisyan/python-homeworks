class Person:
    def __init__(self):
        self._name = None
        self._age = None

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


person = Person()

person.set_name("Lara")
person.set_age(24)

username = person.get_name()
user_age = person.get_age()

print("Name:", username)
print("Age:", user_age)
