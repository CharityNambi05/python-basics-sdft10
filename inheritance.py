# Inheritance in OOP python programming

#Inheritance is a way of creating a new class for using details of an existing class without modifying it.

class Animal:
    def __init__(self, name, color):
        self.name = name 
        self.color = color

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def walk(self):
        print(f"{self.name} is walking")

    def bark(self):
        print(f"{self.name} is barking")

#create an instance of my class
animal_one = Animal("Lion", "Yellow")

print(animal_one.name) # Lion
animal_one.eat() # Lion is eating


class Mammal(Animal):
    pass 

class Dog(Mammal):
    pass
dog_one=Dog("Rono" ,"Orange")

mammal_one = Mammal("James Kahwai", "Black")
mammal_two = Mammal("Sylvia Wanjiku", "Brown") 

mammal_one.eat() # James Kahwai is eating
dog_one.bark()