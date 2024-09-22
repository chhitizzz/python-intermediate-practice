# Create a class Person with attributes first_name and last_name, and a method get_full_name(). Create a subclass Employee that inherits from Person and adds attributes employee_id and position. Implement a method in Employee called get_employee_details() that returns the full name, employee ID, and position.

class Person: 
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self) -> None:
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id: int, position: str) -> None:
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.position = position

    def get_employee_details(self) -> None:
        print(f"My name is {self.get_full_name()}. My position is {self.position} and my employee ID is {self.employee_id}.")

Senna: Employee = Employee("Ayrton", "Senna", 1, "CEO")
Senna.get_employee_details()

Maxwell: Employee = Employee("Glenn", "Maxwell", 2, "Software Developer")
Maxwell.get_employee_details()

George: Employee = Employee("George", "Best", 3, "Automation Engineer")
George.get_employee_details()