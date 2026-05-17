class ZooAnimal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        print(f"{self.name} says Hello")
    def describe(self):
        print(f"{self.name} is a {self.species}")

lion1 = ZooAnimal("Leo", "Lion")
lion1.speak()
lion1.describe()