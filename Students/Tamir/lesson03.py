##FOR LOOP

print("Theory\n")
magic = []
magic.append('Card')
magic.append('Rubik')
print(magic)

for i in magic:
    print(i)    ##Tuhain list dotor bgaa utguudiig hevlene


##To do task 3.1-2
print("Homework: Task 3.1\n")
pizzas = ['pizzahut', 'domingo', 'mr.pizza']
for name in pizzas:
    print(name)
    print(f"I love the  {name.title()}.")
print(f"I really love {pizzas}")

print("\nHomework: Task 3.2")
animals = ['dog', 'cat', 'mouse']
for name in animals:
    print(name)
    print(f"{name.title()} is a pet.")
print(f"{animals} are pets.")


##RANGE
for i in range(1, 11):
    print(i)    ## Range ni interval dotorh utgiig zaana. Ene nuhtsuld 1-10 hurtel toog hevlene.

for i in range(2, 11, 2):
    print(i)    ## 2-s ehleed 11 hurtel toog 2-r alhsaj ogno. End tegsh toonuud hevlegdene

for i in range(1, 10, 2):
    print(i)    ## 1-s ehleed 10 hurtel toog 2-r alhsaj ogno. End sondgoi toonuud hevlegdene

numbers = list(range(1, 11))
print(numbers)

digits = []
for i in range(1, 6):
    digit = i ** 2
    digits.append(digit)
print(digits)

digits = []
for i in range(1, 6):
    digit = i ** 2
    digits.append(digit)
    print(digits)

print(min(digits))
print(max(digits))
print(sum(digits))

letters = ['A', 'B', 'C', 'D']
print(min(letters))
print(max(letters))

squares = [value ** 2 for value in range(1, 11)] ##List dotor davtaltaa hiisen uildel
print(squares)


##WHILE LOOP
a = 10
while(a > 0):
    print(a)
    a = a - 1


##Task 3.3
print("Task 3.3\n")

for i in range(1, 21):
    print(i)

##Task 3.4
print("Task 3.4\n")

end = 21
for i in range(1, end):
    print(i)


##To do Task 3.5-11
print("\nTask 3.5")
end = 21
numbers = []
for i in range(1, end):
    numbers.append(i)
print(numbers)
print(f"Minimum is {min(numbers)}.")
print(f"Maximum is {max(numbers)}.")
print(f"Total is {sum(numbers)}.")


print("\nTask 3.6")
end = 30
numbers = []
for i in range(1, end, 2):
    numbers.append(i)
print(numbers)

print("\nTask 3.7")
start = 3
end = 31
jump = 3
numbers = []
for i in range(start, end, jump):
    numbers.append(i)
print(numbers)


print("\nTask 3.8 and 3.9")
start = 1
end = 11
numbers = []
for i in range(start, end):
    print(f"{i} ** 3 = {i ** 3}")
    y = i**3
    numbers.append(y)
print(numbers)

print("\nTask 3.10")
new_numbers_list = numbers[0:3]
print(new_numbers_list)
newly_list = new_numbers_list[1]
print(newly_list)

print("\nTask 3.11")
my_favorite = pizzas  ##From 3.1
friend_pizzas = my_favorite
for mine in my_favorite:
    print(mine.upper())

for him in friend_pizzas:
    print(him.title())


print("\nTUPLE")
##TUPLE  - Utgiig ni oorchilj bolohgui list
dimensions = (1, 3, 5, 7, 11, 13, 17, 19)
print(dimensions)
print(dimensions[-1])
##dimensions[0] = 1_000_000  ##Utga ni oorchloh bolomjgui tul aldaa zaana


##Task 3.12
print("Task 3.12\n")

foods = ('Гуляш', 'Цуйван', 'Бифштекс', 'Зайдас', 'Бууз')
print(foods)
##foods[0] = 'Мантуу'
##foods.append = ('Хуушуур')


##IF CONDITIONAL

cars = ['toyoto', 'nissan', 'honda', 'suzuki', 'ford']
for car in cars:
    if car == 'ford':
        print(car.title() + " is American car.")
    else:
        print(car.title() + " is Asian car.")

if 'toyoto' in cars:  ##Cars dotor toyoto baina uu.
    print("Yes\n")
else:
    print("No\n")

if 'lincoln' not in cars:  ##Cars dotor lincoln bhgui yu
    print("Yes\n")
else:
    print("No\n")


if 'bmw' in cars:
    print("Yes")
elif 'bentle' in cars:
    pass            ## Pass ni yamar 1 uildel hiilgui tsaash urgeljilne
else:
    print("haha")


##To do task 3.13-19
print("\nTask 3.13")
car_name = 'ford'
car = ''

while(True):
    car = input("Car name: ") ## INPUT - Garaas utga avna
    if car_name == car:
        print("I can predicted")
        break
    else:
        print("I cannot predicted")
        continue


print("\nTask 3.14")
text1 = input("Text1 :")
text2 = input("Text2 :")

if (text1 == text2):
    print(f"{True} : {text1.lower()} - {text2.lower()}")
else:
    print(False)


number1 = input("Number 1 :")
number2 = input("Number 2 :")

if (number1 == number2):
    print(f"{number1} = {number2}")
elif (number1 > number2):
    print(f"{number1} > {number2}")
elif (number1 < number2):
    print(f"{number1} < {number2}")


print("\nTask 3.14")
number1 = input("Number 1 :")
number2 = input("Number 2 :")

if (number1 == number2 or number1 > number2):
    print(f"{number1} => {number2}")
else:
    print(f"{number1} < {number2}")


searching = int(input("Searching number: "))
if searching in numbers:
    print("Your number is contained")
else:
    print("Your number is not contained")
    print(numbers)



print("\nTask 3.15-3.16")
alien = ['Green', 'Yellow', 'Red']
while(True):
    color = input("Alien's color: ")
    if color.title() in alien:
        print(f"{color.title()} alien is died. Earned score: 5")
        break
    else:
        print(f"There is no {color.title()} alien. Earned score: 10")
        continue



print("\nTask 3.20")
usernames = ['Sainaa', 'Admin', 'Tsetsegee', 'Batka', 'Doljko']
user = input("Username: ")
for username in usernames:
    if username == user.title():
        print(f"Hello, {username}. I love you")
    else:
        print(f"Hello, {username}. Thank you")


print("\nTask 3.22")
current_users = ['Sainaa', 'Admin', 'Tsetsegee', 'Batka', 'Doljko']
print(len(current_users))
new_users = ['tamir', 'khangai', 'admin']
count = 0
for n_user in new_users:
    for c_user in current_users:
        if (c_user.upper() == n_user.upper()):
            pass
        else:
            count = count + 1

    if (count == len(current_users)):
        print(f"{n_user} is available")
    elif (count < len(current_users)):
        print(f"{n_user} is not available")

    count = 0


print("\nTask 3.23")
ordinal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in ordinal:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")