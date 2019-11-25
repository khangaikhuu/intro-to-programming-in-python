##Task 4.1
print("Task 4.1\n")
my_friend = {}
my_friend['first_name'] = 'Tamir'
my_friend['last_name'] = 'Bold'
my_friend['age'] = 35
my_friend['city_name'] = 'UB'
print(my_friend)
print(my_friend['first_name'])
print(my_friend['last_name'])
print(my_friend['age'])
print(my_friend['city_name'])


##Task 4.2
print("\nTask4.2")
fav_number = {}
for i in range(1, 6):
    name = input("Name: ")
    number = input("Number: ")
    fav_number[name] = number

for i, j in fav_number.items():
    print(f"{i}'s favorite number is {j}.")


##Task 4.4
print("\nTask 4.4")
famous_rivers= {
    'bold' : 'father',
    'enerel' : 'mother',
    'seseer' : 'me'
}

for key, value in famous_rivers.items():
    print(f"The {key.title()} is a {value.title()}.")

for key in famous_rivers.keys():
    print("\t"+key.title())

for value in famous_rivers.values():
    print(value.title())