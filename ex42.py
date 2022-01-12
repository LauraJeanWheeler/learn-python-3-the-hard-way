# Animal is-a object 
# Use the pass keyword when you do not want to add any other properties or methods to the class.
class Animal(object):
    pass

# Dog has-a name
class Dog(Animal):
    def __init__(self, name):
        self.name = name

# Cat has-a name
class Cat(Animal):
    def __init__(self, name):
        self.name = name

# Person has-a name
class Person(object):
    def __init__(self, name):
        self.name = name 
    # Person has-a pet of some kind
        self.pet = None

# Employee has an instance of a person
# person has-a instance, name, and salary
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary 

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a fish
class Salmon(Fish):
    pass

# Halibut is-a fish
class Halibut(Fish):
    pass

# Rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# Mary is-a person
mary = Person("Mary")

# Mary has-a pet cat named satan
mary.pet = satan

# Frank is an Employee, who has-a salary of 120k
frank = Employee("Frank", 120000)

# Frank has a pet dog named rover
frank.pet = rover

# Flipper is-a fish
flipper = Fish

# Crouse is a Salmon
crouse = Salmon()

# Harry is a Halibut
harry = Halibut()