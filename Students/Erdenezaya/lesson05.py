class Restaurant:
    def __init__(self):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name} and we serve {self.cuisine_type}")    
    def open_restauratn(self):
        print("The restaurant is open")
khangai_pub = Restaurant(self)
khangai_pub.describe_restaurant()
khangai_pub.open_restauratn()

from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_die(self):
        print(randint(1, self.sides))
die1 = Die()
die1.roll_die()
die2 = Die(12)
die2.roll_die()