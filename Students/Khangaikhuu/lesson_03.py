# 3 Working with Lists and Conditionals
# 3.1 Looping through in a List
magicians = ['alice', 'david', 'carolina']

# Latex / Knuth / Literal programming/ MMIX - 64Bits
# 8 Bits
# 0/1 Bit 32 bits/ 64 bits
# A = 010101011100101101...001
# 0101010101101111 - WRITE
# 0101011111011111 - STORE
for j in magicians:
    print(j)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

#Indentation error
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

message = "Hello Python world!"
print(message)

# Forgetting the colon
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


# Exercises
"""
Ex-3.1 
Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
• Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!

Ex-3.2
Think of at least three different animals that have a common char-
acteristic. Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
• Modify your program to print a statement about each animal, such as
A dog would make a great pet.
• Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
"""

# Range function
for i in range(1, 5):
    print(i)

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)
# even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)

# strict - indentation
# BUG - code error/code fault/system fault
# Ada Lovelace / Ada 
# https://upload.wikimedia.org/wikipedia/commons/8/8a/H96566k.jpg
# https://en.wikipedia.org/wiki/Software_bug
# 

# min, max, sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# Build 
squares = [value**2 for value in range(1, 11)]
print(squares)

while(True): # python condition
    print("Hello")
"""
Ex.3.3
Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
Ex.3.4
One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl -C or by closing the output window.)
Ex.3.5
Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
Ex.3.6
Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.
Ex.3.7
Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
Ex.3.8
Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
Ex.3.9
Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

"""
Ex.3.10
Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Use a slice to
print three items from the middle of the list.
• Print the message The last three items in the list are:. Use a slice to print the
last three items in the list.

Ex.3.11
My Pizzas, Your Pizzas: Start with your program from Exercise 3.1. 
Make a copy of the list of pizzas, and call it friend_pizzas .
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas .
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.
"""

# 3.2 TUPLES
# However, sometimes you’ll want to 
# create a list of items that cannot change. 
# List - mutable
# Python refers to values that cannot change 
# as immutable, 
# and an immutable list is called a tuple.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200, 50)
dimensions[0] = 250

my_t = (3,)

dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

"""
Ex.3.12
Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""

# IF statements
#
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Conditional Tests
# ==/ != / < / > / <= / >=
car = 'audi'
car == 'bmw'
car.lower() == 'audi'
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 10
age < 21
age <= 21
age > 21
age >= 21

# Multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
age_0 >= 21 or age_1 >= 21
# use in IF / WHILE

# 0 -> False
# 1 -> True
# AND   0 0 -> 0
#       1 0 -> 0
#       0 1 -> 0
#       1 1 -> 1

# OR    0 0 -> 0
#       1 0 -> 1
#       0 1 -> 1
#       1 1 -> 1

#Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

"""
Ex.3.13 
Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False .
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False .

Ex.3.14
More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
elif age > 45:
    pass
else:
    print("Your admission cost is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

"""
Ex.3.15
Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red' .
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)

Ex.3.16
Alien Colors #2: Choose a color for an alien as you did in Exercise 3.15, and
write an if - else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.

Ex.3.17
Alien Colors #3: Turn your if - else chain from Exercise 3.16 into an if - elif -
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.

Ex.3.18

Stages of Life: Write an if - elif - else chain that determines a person’s
stage of life. Set a value for the variable age , and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.

Ex.3.19
Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits .
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

"""
Ex.3.20 
Hello Admin: Make a list of five or more usernames, including the name
'admin' . Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin' , print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.

Ex.3.21
No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.

Ex.3.22
Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users .
• Make another list of five usernames called new_users . Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)

Ex.3.23
Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if - elif - else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th" , and each result should be on a separate line.
"""

"""
    Guess the number game : 
    This game should gets new random number and remembers it.
    it asks the user a number until user guesses the number.
"""

# User Input

secret_number = 42

while(True): # infinite Loop
    user_input = int(input("Give me a number: "))
    if secret_number == user_input:
        print("You won!!!")
        break
    elif secret_number > user_input:
        print("It's hot")
    elif secret_number < user_input:
        print ("It's cold")
    else:
        continue



