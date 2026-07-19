# Demonstrate method overriding

class Animal:

    def sound(self):
        print("Animals make sounds")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()
