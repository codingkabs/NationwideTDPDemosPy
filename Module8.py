class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def speak(self):
        return self.name + " says hi!"

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Bike:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

person_jordan = Person("Jordan", 20, "Trainer")
person_liang = Person("Liang", 25, "Student")

person_jordan.speak()
person_liang.speak()