# Lesson 03 Homework assignment
# 3 Working with Lists and Conditional statements and Input function
# 3.1 Looping through in a List and Tuple
# ---------------------------------
import random
import os
def clr():
    os.system('cls')

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
"""
print("# 3.1")
pizza=["Hawai pizza", "Cheese pizza", "Tuna pizza"]
for i in pizza:
    print(f"I like {i}")
print("I really love pizza")
clr()
"""
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
print("# 3.2")
animal=["crows", "woodpecker", "orioles"]
for item in animal:
    print("A {} is a fascinating bird".format(item))
print("Any such kind of birds might be manage to unerringly travel between distance location to migrate ")

clr()
"""
Ex.3.3
Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
"""
print("# 3.3")
count=0
for i in range(1, 20+1 ):
    count=count+1
print("Total numbers between 1 to 20 is", count)
clr()
"""
Ex.3.4
One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl -C or by closing the output window.)
"""
print("# 3.4")
million=list(range(1,10)) # it is done already range in one million
for i in million:
    print(i)

clr()
"""
Ex.3.5
Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
"""
print("# 3.5")
million=list(range(1,1000000+1))
min_num=min(million)
print(min_num)
max_num=max(million)
print(max_num)
sum_num=sum(million)
print(sum_num)
clr()
"""
Ex.3.6
Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.
"""
print("# 3.6")
for i in range(1, 20, 2):
    print(i)

clr()
"""
Ex.3.7
Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
"""
print("# 3.7")
Threes=[item for item in list(range(0,30)) if item%3==0]
for i in Threes:
    print(i)

clr()
"""
Ex.3.8
Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
"""
print("# 3.8")
cubes=[item**3 for item in range(1,11) ]
for i in cubes:
    print(i)
"""
Ex.3.9
Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""

print("# 3.9")

for comprehension in range(1, 11):
    cubes=[item**3 for item in range(comprehension+1) ]
    print(cubes)


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
"""
print("# 3.10")
cubes=[item**3 for item in range(1,11) ]
print(cubes)
print("The first three items in the list are:", cubes[:3])
print("The middle three items in the list are:", cubes[int(len(cubes)/2-1):int(len(cubes)/2)+2])
print("The last three items in the list are:", cubes[-3:])

"""
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
print("# 3.11")
my_pizza=["Hawai pizza", "Cheese pizza", "Tuna pizza"]
friend_pizzas=["Hawai pizza", "Cheese pizza", "Tuna pizza"]
my_pizza.append("Zaidsan Delbeet")
friend_pizzas.append("Mix pizza")
print("My fav pizzas are ",my_pizza)
print("Friend fav pizzas are ", friend_pizzas)
for i in friend_pizzas:
    print("Friend fav pizzas is ", i)

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
print("# 3.12")
buffet=("BBQ pork", "Shrimp scampi", "Seafood Alfredo", "Roast beef", "Paste with chicken")
print("This restaurant menu is:")
for i in buffet:
    print("\t", i)
#buffet[0]="Pizza"  TypeError: 'tuple' object does not support item assignment
buffet_list=list(buffet)
buffet_list[2]="Tuna steak"
buffet_list[3]="Lamb soup"
buffet=tuple(buffet_list)
print("This restaurant NEW menu is:")
for i in buffet:
    print("\t", i)
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
"""
print("# 3.13")
cars=["Tesla", "LX770", "Forche", "Toyoto hybrid"]
print("Is car == 'subaru'? I predict True as.", cars[0]=="Tesla")
print(cars[0] == 'subaru')
print("\nIs car == 'audi'? I predict False.", cars[1] == 'subaru')
print(cars[1] == 'subaru')
"""

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
print("# 3.14")


"""
Ex.3.15
Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red' .
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
"""
print("# 3.15")
alien_color=['green' , 'yellow' , 'red']
select=random.choice(alien_color)
if select=='green':
    print("You got 5 points")
else:
    print("Passed, but you lost -5 points")


"""
Ex.3.16
Alien Colors #2: Choose a color for an alien as you did in Exercise 3.15, and
write an if - else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
"""
print("# 3.16")
"""
Ex.3.17
Alien Colors #3: Turn your if - else chain from Exercise 3.16 into an if - elif -
else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.

"""
print("# 3.17")


"""
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
"""
print("# 3.18")

"""

Ex.3.19
Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits .
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""
print("# 3.19")



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
"""
print("# 3.20")
"""
Ex.3.21
No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
"""
#print("# 3.21")

"""

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
"""

#print("# 3.22")

"""
Ex.3.23
Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if - elif - else chain inside the loop to print the proper ordinal end-
ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th" , and each result should be on a separate line.
"""
#print("# 3.23")

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



