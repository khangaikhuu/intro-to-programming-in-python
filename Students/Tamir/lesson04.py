##Task 4.3
print("Task 4.3\n")
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

##Task 4.3
print("\nTask 4.4\n")
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
