from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Cat(IAnimal):
    def speak(self):
        print("Meow!")

    def eat(self):
        print("Cat is eating.")

class Dog(IAnimal):
    def speak(self):
        print("Woof!")

    def eat(self):
        print("Dog is eating.")


cat = Cat()
dog = Dog()

cat.speak()
cat.eat()

dog.speak()
dog.eat()
