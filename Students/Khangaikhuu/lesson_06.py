# 6. Classes
# Object = Instance
# 

def F():
    def calculate_min(x, y):
        if (x > y):
            return x
        else:
            return x > y
    def G():
        print("Its G")
    g = F.G
    print (g)
    print(calculate_min(1,3))
    print ("Its F")

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Battery class
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

# Loosely coupled -> 

# Test-1
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Test-2
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()



"""
Ex.5.1 Restaurant: Make a class called Restaurant . The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type .
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"My restaurant name is {self.restaurant_name} and we serve {self.cuisine_type}")
    def open_restaurant(self):
        print("The restaurant is open")

khangai_pub = Restaurant("Nice Wine", "wines")
khangai_pub.describe_restaurant()
khangai_pub.open_restaurant()

"""
Ex.5.2. Three Restaurants: Start with your class from Ex.5.1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

Ex.5.3. Users: Make a class called User . Create two attributes called first_name
and last_name , and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.

Ex.5.4. Number Served: Start with your program from Ex.5.1.
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.

Ex.5.5. Login Attempts: Add an attribute called login_attempts to your User
class from Ex.5.3. Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts() . Print login_attempts again to
make sure it was reset to 0.

Ex.5.6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Ex.5.1 or Ex.5.4. Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand , and call this method.

Ex.5.7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Ex.5.3
or Ex.5.5. Add an attribute, privileges , that stores a list
of strings like "can add post" , "can delete post" , "can ban user" , and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin , and call your method.

Ex.5.8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges , that stores a list of strings as described in Ex.5.7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.

Ex.5.9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery() . This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
"""

# Importing a class
from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Importing multiple classes
from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# Importing an entire module
# Facebook Lite
import car
my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# Using Aliases
from car import Car as C, ElectricCar as EC
my_tesla = EC('tesla', 'roadster', 2019)

# The Python Standard Library
from random import randint
randint(1, 6)


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        message_parts = [
            'CLIENT VALUES:',
            'client_address={} ({})'.format(
                self.client_address,
                self.address_string()),
            'command={}'.format(self.command),
            'path={}'.format(self.path),
            'real path={}'.format(parsed_path.path),
            'query={}'.format(parsed_path.query),
            'request_version={}'.format(self.request_version),
            '',
            'SERVER VALUES:',
            'server_version={}'.format(self.server_version),
            'sys_version={}'.format(self.sys_version),
            'protocol_version={}'.format(self.protocol_version),
            '',
            'HEADERS RECEIVED:',
        ]
        for name, value in sorted(self.headers.items()):
            message_parts.append(
                '{}={}'.format(name, value.rstrip())
            )
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
"""
Ex.6.1 
Dice: Make a class Die with one attribute called sides , which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint

class Die:
    def __init__(self, begin=1, end= 6):
        self.begin = begin
        self.end = end
    def roll_die(self):
        print(randint(self.begin, self.end))

die1 = Die()
die1.roll_die()

die2 = Die(end=12)
die2.roll_die()

die3 = Die(1000, 99_999)
die3.roll_die()


"""
Ex.6.2 
Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.

Ex.6.3
Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket .
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.

Ex.6.4
Python Module of the Week: One excellent resource for exploring the
Python standard library is a site called Python Module of the Week. Go to
https://pymotw.com/ and look at the table of contents. Find a module that
looks interesting to you and read about it, perhaps starting with the random
module.
"""

# Reading files
# Files and Exceptions/ Runtime Error
# Reading from a File


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

file_path = '/home/khangaikhuu/Desktop/intro-to-programming-in-python/Students/Khangaikhuu/pi_digits.txt'
file_path_windows = 'C:/Users/khangaikhuu/'
with open(file_path) as file_object:
    pass

# "C:\\path\\to\\file.txt" .
# Reading Line by Line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

# Making a List of Lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# Working with a File’s Contents
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

"""
Ex.6.5 
Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by stor-
ing the lines in a list and then working with them outside the with block.
Ex.6.6
Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

# Writing to a File
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
# read mode ( 'r' ), write mode ( 'w' ), append mode ( 'a' ), 
# or a mode that allows you to read and write to the file ( 'r+' ).

# Writing Multiple Lines
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# Appending to a File
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

"""
Ex.6.7
Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.

Ex.6.8
Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.

Ex.6.9
Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

# 7. Exceptions
# Handling the ZeroDivisionError Exception
print(5/0)

# Using try-except Blocks
import sys
try:
    print(5/0)
except Exception as e:
    print( "<p>Error: %s</p>" % str(e) )

try:
    int(input("Give me a number: "))
except ValueError:
    print(" You cannot give a text for number")

# Using Exceptions to Prevent Crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    answer = int(first_number) / int(second_number)
    # !!! 
    print(answer)

# Handling the FileNotFoundError Exception
filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()









filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")



# Analyzing Text
filename = 'alice.txt'
# http://www.gutenberg.org/ 
# Alice in Wonderland

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# Working with Multiple Files
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:      
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'alice.txt'
count_words(filename)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# Failing Silently

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


"""
Ex.7.1
Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly.

Ex.7.2
Silent Cats and Dogs: Modify your except block in Ex.7.1 to fail
silently if either file is missing.

Ex.7.3
Common Words: Visit Project Gutenberg (https://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there' .
Try counting 'the ' , with a space in the string, and see how much lower your
count is.
"""

# Storing data
"""
The json module allows you to dump simple Python data structures into a
file and load the data from that file the next time the program runs. You can
also use json to share data between different Python programs. Even better,
the JSON data format is not specific to Python, so you can share data you
store in the JSON format with people who work in many other programming
languages. It’s a useful and portable format, and it’s easy to learn.
"""

# json.dump()
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

# json.load()
import json
with open(filename) as f:
    numbers = json.load(f)

print(numbers) 

# Saving and Reading User-Generated Data
import json
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")


import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")


import json
def get_stored_username():
    """Greet the user by name."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

"""
Ex.7.4
Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”

Ex.7.5
Favorite Number Remembered: Combine the two programs from
Ex.7.4 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""

# PS 
# AI
# Tensor Flow - Google Software
# Watson Assistant - IBM - API - AI
# https://machinelearningforkids.co.uk/#!/worksheets

# Next Chapter
# Testing your code
# Testing a function
# Testing a class

def calc_addition(a, b):
    return a + b

calc_addition(4, 5) == 9
calc_addition(4, 8) == 12
calc_addition(1, 2) == 3
calc_addition(4, 1) == 5
calc_addition(-1, 1) == 0

if calc_addition(4, 5) == 9:
    print ("Your function is correct")
else:
    print ("Your function is false")