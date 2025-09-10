class Person:
    def __init__(self, name, occupation, organization):
        self.name = name
        self.occupation = occupation
        self.organization = organization
    def describe(self):
        print(f"My name is {self.name}, work as {self.occupation}, at  {self.organization}")

# create an object
person = Person("Malik", "Analyst", "Malik_Foundation")   
person.describe()     


# create other classes
class Manager:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
    def display(self):
        print(f"My name is {self.first_name} {self.last_name}")

manager = Manager("Madrine", "Nalukwago")   
person.display()     


# this is our last meeting
x = 10
# y = 20
# z = x + y
