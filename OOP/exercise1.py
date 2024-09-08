# Create a class Person with attributes name and age. Include a method greet() that prints "Hello, my name is name and I am age years old". Create an instance of Person and call the greet() method.

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

        