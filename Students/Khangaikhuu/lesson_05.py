# # Python Classes
# 
# Object-oriented programming is one of the
# most effective approaches to writing soft-
# ware. In object-oriented programming you
# write classes that represent real-world things
# and situations, and you create objects based on these
# classes. When you write a class, you define the general
# behavior that a whole category of objects can have.

# functional programming - Abstraction
# imperative programming
# object oriented programming - Abstraction
# inheritance -> 


# Creating the Dog Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Accessing Attributes
my_dog.name
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()


# Creating Multiple Instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

"""
Ex.5.1 
Restaurant: Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.

Ex.5.2. 
Three Restaurants: Start with your class from Exercise 5.1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

Ex.5.3 
Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
# Setting a Default Value for an Attribute

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.manifacturer = "Tesla"
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def change_odometer(self, new_val):
        if new_val < 1000:
            self.change_odometer = new_val
        else:
            self.change_odometer = 999

    
# Encapsulation information hiding

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute’s Value Directly 

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method

# def update_odometer(self, mileage):
#    """Set the odometer reading to the given value."""
#    self.odometer_reading = mileage

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# Inheritance/ Extension
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
        self.self_driving = True
    def read_odometer(self): # Overwrite
        """Print a statement showing the car's mileage."""
        print(f"No i have not Odometer")
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


class Animal:
    def __init__(self, character):
        self.character = character
    
    def make_sound(self):
        print(f"I can {self.character}")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
        self.canBell = True
    def make_sound(self):
        print (f"i can Bell")


class Cat(Animal):
    def __init__(self):
        super().__init__("C")
        self.canBell = False
    def make_sound(self):
        print (f"i can Meow")