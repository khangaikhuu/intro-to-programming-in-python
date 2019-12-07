# Lesson 5 Homework assignment
# Python Classes 
# Object-oriented programming is one of the
# most effective approaches to writing software. In object-oriented programming you
# write classes that represent real-world things
# and situations, and you create objects based on these
# classes. When you write a class, you define the general
# behavior that a whole category of objects can have.

# functional programming - Abstraction
# imperative programming
# object oriented programming - Abstraction
# inheritance -> 
# ---------------------------------


"""
Ex.5.1 
Restaurant: Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""
print("# 5.1")
class Restaurant2:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served=number_served
    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name} and we serve {self.cuisine_type}")
    def open_restaurant(self):
        print("The restaurant is open")
    def set_number_served(self):
        print(f"{self.number_served} customers were served in a day of business.")

rest = Restaurant2("GMJ", "lamb" ,7)
rest.describe_restaurant()
rest.open_restaurant()
rest.set_number_served()


"""
Ex.5.2. 
Three Restaurants: Start with your class from Exercise 5.1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""
print("# 5.2")
rest1 = Restaurant2("GMJ1", "lamb1" ,7)
rest1.describe_restaurant()
rest2 = Restaurant2("GMJ2", "lamb2" ,7)
rest2.describe_restaurant()
rest3 = Restaurant2("GMJ3", "lamb3" ,7)
rest3.describe_restaurant()
"""

Ex.5.3 
Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
print("# 5.3")
class User:
    def __init__(self, first_name, last_name ):
        self.first_name=first_name
        self.last_name=last_name
        self.age=27
        self.gender="Male"
        self.major="Finance"
    def describe_user(self):
        print(f"His first name is {self.first_name}, last name is {self.last_name}, He is {self.age} year old. ")

    def greet_user(self):
        print("Hello World, Welcome to my tour")



fagui=User("Manasha", "Natasha")
fagui.describe_user()
fagui.greet_user()

riben=User("Manasan", "Munusun")
riben.describe_user()
riben.greet_user()


