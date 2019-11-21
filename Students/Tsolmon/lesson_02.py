# Lesson 02
# ---------------------------------
# 1. Python Strings
name = "ada lovelace"

#1.1 python string methods
print(name.title())
print(name.upper())

first_name = "ada"
last_name = "lovelace"

#1.2. python f string
full_name = f"{first_name}{last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

# 1.3 format string
full_name = "{} {}".format(first_name, last_name)

# 1.4 new line and tab
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 1.5 rstrip()/lstrip()/strip()
favorite_language = 'python '
favorite_language.rstrip()
favorite_language = favorite_language.rstrip()
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

# 1.6 comments
"""
dfdfdfdfd
dfdfdfd
"""

# 1.7 Exercises
"""
1.1 -  Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?”

1.2 - Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.

1.3 - Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks:
    Albert Einstein once said, “A person who never made a
        mistake never tried anything new.”

1.4 - Repeat Exercise 1.3, but this time, represent the
famous person’s name using a variable called famous_person . Then compose
your ­message and represent it with a new variable called message . Print your
message.

1.5 - Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n" , at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip() ,
rstrip() , and strip() .
"""
# 2.1 Lists and integer types
universe_age = 14_000_000_000
x, y, z = 0, 0, 0
MAX_CONNECTIONS = 5000

"""
In this chapter and the next you’ll learn
what lists are and how to start working with
the elements in a list. Lists allow you to store
sets of information in one place, whether you
have just a few items or millions of items. Lists are
one of Python’s most powerful features readily acces-
sible to new programmers, and they tie together many
important concepts in programming.
"""

# Strong typed language = Java, C, C++
# dynamic/loosely typed language = PHP, Python, Javascript -> 
# Typescript - AngularJS - Google
# VueJS - Typescript
# Backend - server side process  (Java Python - Flask/Django C node js - ExpressJS, BackboneJS)
# FrontEnd - JS -> ReactJS, AngularJS, VueJS
# Heroku/ AWS (Amazon web server)
# Microservices
# Deployment

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicyle = ['trek', 1, True]

print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
"""
Ex-2.1 - Store the names of a few of your friends in a list called names . Print
each person’s name by accessing each element in the list, one at a time.

Ex-2.2 - Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle".
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# 2.2 insert/delete elements from list 
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
a = motorcycles[-1]
# Stack  
# 
# 1
# 2
# 3

# def a(name ):
#       b = 0 --> Closure/ local variable
# b = 0

print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
"""
Ex-2.3 - If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""
invitation_list = ['zuckerberg','elon','watson']
print(f"{invitation_list[0].title()}, You are invited")
print(f"{invitation_list[1].title()}, You are invited")
print(f"{invitation_list[2].title()}, You are invited")
"""
Ex-2.4 - You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
    • Start with your program from Ex-2.3. Add a print() call at the end
    of your program stating the name of the guest who can’t make it.
    • Modify your list, replacing the name of the guest who can’t make it with
    the name of the new person you are inviting.
    • Print a second set of invitation messages, one for each person who is still
    in your list.
"""
print(f"{invitation_list[2]} can't come to the dinner")
invitation_list.remove('watson')
invitation_list.append('harry potter')
print(f"{invitation_list[2].title()}, You are invited to the dinner")

"""
Ex-2.5 - You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
    • Start with your program from Ex-2.3 or Ex-2.4. Add a print()
    call to the end of your program informing people that you found a bigger
    dinner table.
    • Use insert() to add one new guest to the beginning of your list.
    • Use insert() to add one new guest to the middle of your list.
    • Use append() to add one new guest to the end of your list.
    • Print a new set of invitation messages, one for each person in your list.

Ex-2.6 - You just found out that your new dinner table won’t
    arrive in time for the dinner, and you have space for only two guests.
    • Start with your program from Ex-2.5. Add a new line that prints a
    message saying that you can invite only two people for dinner.
    • Use pop() to remove guests from your list one at a time until only two
    names remain in your list. Each time you pop a name from your list, print   
    a message to that person letting them know you’re sorry you can’t invite    
    them to dinner.
    • Print a message to each of the two people still on your list, letting them
    know they’re still invited.
    • Use del to remove the last two names from your list, so you have an empty
    list. Print your list to make sure you actually have an empty list at the end
    of your program.
"""
# 2.5 Organize your lists sort()/reverse()/sorted() functions
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
# searching ()
# $$$$$$$$$$$$$$$$$$
# sorting algorithm

print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 2.6 Length of the list
len(cars)

"""
    Ex-2.7 
    Think of at least five places in the world you’d like to visit.
    • Store the locations in a list. Make sure the list is not in alphabetical order.
    • Print your list in its original order. Don’t worry about printing the list neatly,
    just print it as a raw Python list.
    • Use sorted() to print your list in alphabetical order without modifying the
    actual list.
    • Show that your list is still in its original order by printing it.
    • Use sorted() to print your list in reverse alphabetical order without chang-
    ing the order of the original list.
    • Show that your list is still in its original order by printing it again.
    • Use reverse() to change the order of your list. Print the list to show that its
    order has changed.
    • Use reverse() to change the order of your list again. Print the list to show
    it’s back to its original order.
    • Use sort() to change your list so it’s stored in alphabetical order. Print the
    list to show that its order has been changed.
    • Use sort() to change your list so it’s stored in reverse alphabetical order.
    Print the list to show that its order has changed.

    Ex-2.9
    Think of something you could store in a list. For example,
    you could make a list of mountains, rivers, countries, cities, languages, or any-
    thing else you’d like. Write a program that creates a list containing these items
    and then uses each function introduced in this chapter at least once.
"""

#Important!!!
# Using index a list is sometimes error prone
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

#Instead of using index
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

