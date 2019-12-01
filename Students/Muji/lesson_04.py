# Lesson - 04 Homework assignment
# Dictionaries
# What is a dictionary datastructure?
# Define functions
# ---------------------------------


"""
Ex-4.1
Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name , last_name , age , and city . 
Print each piece of information stored in your dictionary.
"""
print("# 4.1")
person={"first_name":'GMJ' , "last_name":"GNKHG" , "age":18 , "city":"Erdenet"}
for key, value in person.items():
    print(f" {key} is {value}")

"""
Ex-4.2. 
Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""
#print("# 4.2")

"""
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
print("# 4.3")
glossary={"stash":"keep file in different place", "convention":"agreement", "poll":"ask questions"}
for key, value in glossary.items():
    print(f"\n {key} : \n\t{value} ")

"""
Ex.4.4
Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt' .
• Use a loop to print a sentence about each river, such as f"The Nile runs
through Egypt". items() ('nile', 'egypt')
• Use a loop to print the name of each river included in the dictionary.  keys()
• Use a loop to print the name of each country included in the dictionary. values()
"""
#print("# 4.4")

"""
Ex. 5.1
Write a function called display_message() that prints one sen-
tence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
"""
print("# 5.1")
def display_message():
    print("I am learning dictionary and function in this chapter")
"""
Ex. 5.2
Favorite Book: Write a function called favorite_book() that accepts one
parameter, title . The function should print a message, such as One of my
favorite books is Alice in Wonderland . Call the function, making sure to
include a book title as an argument in the function call.
"""
#print("# 5.2")

"""
Ex.5.3
T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""
#print("# 5.3")

"""
Ex.5.4
Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.

"""
#print("# 5.4")

"""
Ex.5.5
Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland . Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
"""
print("# 5.5")
def describe_city(city="Manila", country="Phillipine"):
    print(f" {city} is in {country}.")


describe_city("Reykjavik", "Iceland")
describe_city()
describe_city("Boracay")

"""
Ex.5.6
City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""
#print("# 5.6")

"""
Ex. 6.1
Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
"""
print("# 6.1")
print("Run printing_function_06.py")
"""
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
#print("# 6.2")


