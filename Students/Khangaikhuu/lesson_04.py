# Lesson - 04

# Dictionaries
# What is a dictionary datastructure?

alien_0 = {
    'color': 'green', 
    'points': 5, 
    'x_position' : 5.0, 
    ' y_position': 6.0}
# keys : color, points
# values : green, 5
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green'}
# Accessing Values in a Dictionary
print(alien_0['color'])
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['family_name'])

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 5.0)
print(point_value)

"""
Ex-4.1
Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name , last_name , age , and city . 
Print each piece of information stored in your dictionary.

Ex-4.2. 
Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
Ex.4.3 
Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
lesson. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character ( \n ) to insert a blank line between each word-meaning
pair in your output.
"""
# Looping Through a Dictionary
# Iterable : i can loop in dictionary

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping Through All the Keys in a Dictionary
# The keys() method is useful when you don’t
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'uvgunkhuu': 'c++',
    'khangai': 'ruby',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:") 
# distinct , no duplicated values / unique
for language in set(favorite_languages.values()):
    print(language.title())
"""
Ex.4.4
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt' .
• Use a loop to print a sentence about each river, such as f"The Nile runs
through Egypt". items() ('nile', 'egypt')
• Use a loop to print the name of each river included in the dictionary.  keys()
• Use a loop to print the name of each country included in the dictionary. values()
"""
rivers = {
    'nile':'egypt',
    'orkhon': 'mongolia',
    'amazon' : 'brazil'
}

for i, j in rivers.items():
    print(f"The {i.title()} runs through {j.title()}")

for i in rivers.keys():
    print (i)

for i in rivers.values():
    print (i)

# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien_3 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]: # inclusive, exclusive
    print(alien)
    print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
# scheme, lisp, ocaml - functional programming languages
# programming language syntax is very hard to understand in functional programming language

# functional programming language
# c/ c++/ java - imperative object oriented programming languages
#   state a = 10;
# functional - this language has only functions
# f(x) = x * x
# f(5) = 25
# functional programming has no side effects
# c/c++ => f(5) = 36
# c/c++ => f(5) = 26
# side effects

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

for language in languages:
    print(f"\t{language.title()}")


# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


"""
Game Programming: 
Count all the words for given input and save the words into dictionary with its 
number of occurences in the sentence.

Input  : "This should be enough to store each word in a list. 
words is already a list of the words from the sentence, 
so there is no need for the loop."

Output : {'This': 2, 'should': 2, 'be': 2, 'enough': 2, 'to': 2, 'store': 2, 'each': 2, '
word': 2, 'in': 2, 'a': 3, 'list.': 2, 'words': 3, 'is': 3, 'already': 2, 'list'
: 2, 'of': 2, 'the': 4, 'from': 2, 'sentence,': 2, 'so': 2, 'there': 2, 'no': 2,
 'need': 2, 'for': 2, 'loop.': 2}
"""
text = "This should be enough to store each word in a list. words is already a list of the words from the sentence, so there is no need for the loop."
splitted_text = text.split()
word_counter = {}
for i in splitted_text:
        if i in word_counter.keys():
            count = word_counter[i]
            count = count + 1
            word_counter[i] = count
        else:
            word_counter[i] = 1
print (word_counter)


def splitter (splitted_text, word_counter_dictionary):
    for i in splitted_text:
        if i in splitted_text.keys():
            count = word_counter_dictionary[i]
            count = count + 1
            word_counter_dictionary[i] = count
        else:
            word_counter_dictionary[i] = 1


# Abstraction ->  2 * 2 = 4 f(x) = x * x
# software -> It should have Abstraction!!!

# 2 * 2 =  2 + 2
# 3 * 3 = 3 + 3 + 3 = 9
# 2 + 2 + 2 + 2 = 2 ^ 3 = 2 ** 3


# 5. Defining a Function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user() # calling a function/ usage of function


# Passing Information to a Function
def greet_user(username): # username - parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse') # argument

# Arguments and Parameters
"""
Ex. 5.1
Write a function called display_message() that prints one sen-
tence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
Ex. 5.2
Favorite Book: Write a function called favorite_book() that accepts one
parameter, title . The function should print a message, such as One of my
favorite books is Alice in Wonderland . Call the function, making sure to
include a book title as an argument in the function call.
"""
# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to con-
# tinue interpreting positional arguments correctly.

# f(x, y) = x + y
# z = f(5, 6)
# 
# Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# null = None

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

# dynamic typed language python name = "6"
# name = 6
# Python interpreter -> Parser -> name = integer -> Python Interpreter Memory name = integer(6)
# name = 6
# Parser -> Syntax Tree -> name  =  6
# Compiler -> Interpreter 
#     =
#   /   \
# name   6
# exp = exp
# variable = name
# exp = 6 = > integer type

# STORE NAME 6
# 1011110111 0010101010 101

# static typed language  int a = 1


# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Fibonacci number
# F(0) = 0
# F(1) = 0
# F(x) = F(x - 1 ) + F(x - 2)    

def F(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return F(x - 1) + F(x - 2)
# 6. Storing Your Functions in Modules

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from module_name import function_name
from pizza import make_pizza
make_pizza(16, 'pepperoni')
from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
import pizza as p

# Module
import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
Ex.5.3
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.

Ex.5.4
Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.

Ex.5.5
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland . Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.

Ex.5.6
City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""

"""
Ex. 6.1
Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.

Ex. 6.2 
Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""

