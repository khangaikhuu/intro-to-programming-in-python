class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"name is {self.restaurant_name} & serve {self.cuisine_type}" )
    def open_restaurant(self):
        print("Open")

pub = Restaurant("Tsolmon","khuushuur")

pub.describe_restaurant()
pub.open_restaurant()
import random as randint

class Die:
    def __init__(self,sides =6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides))