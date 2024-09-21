# Create a base class Animal with attributes name and species, and a method make_sound(). Then create a subclass Dog that inherits from Animal and adds a method fetch(). Instantiate a Dog object and call both methods.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"{self.name} the {self.species} makes a sound.")

# Subclass Dog that inherits from Animal
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")
    
    def fetch(self):
        print(f"{self.name} is fetching the ball!")

my_dog = Dog("Subhu")
my_dog.make_sound()
my_dog.fetch()