##Task 5.1
print("Task 5.1")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name} and we serve {self.cuisine_type}")
    def open_restaurant(self):
        print ("The restaurant is opened")


my_pub = Restaurant('Tamir', 'Sushi')
my_pub.describe_restaurant()
my_pub.open_restaurant()