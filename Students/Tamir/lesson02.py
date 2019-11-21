#Task 1.1
print("Task 1.1")
person_name = "Tamir"
print("Would you like to learn some Python today? " + person_name + "\n");


#Task 1.2
print("Task 1.2")
print(person_name.lower())
print(person_name.title())
print(person_name.upper() + "\n")


#Task 1.3
print("Task 1.3")
default_name = "Albert Einshtein"
print(default_name + ' said "I am famous"' + "\n")
full_name = "{}{}".format(person_name, default_name) ##Format ni tuhain utgiig hoorond ni holboj hevlene
print(full_name)


#Task 1.4
print("Task 1.4")
print("Languages:\nPython\nC\nJavaScript")  ## \n ni new line hiine
print("Languages:\n\tPython\n\tC\n\tJavaScript")  ## \t ni tab avna


#Task 1.5
print("Task 1.5")

print("Task 1.5 - n")
text_message_n = "   My   \n   Family   "
print(text_message_n.strip())
print(text_message_n.lstrip())
print(text_message_n.rstrip() + "\n")

print("Task 1.5 - t")
text_message_t = "   My   \t   Family   "
print(text_message_t.strip())
print(text_message_t.lstrip())
print(text_message_t.rstrip() + "\n")


#Task 2.1
print("Task 2.1")
dynamic_variable = ['Tamir', 37, True]
print(dynamic_variable)
print("My name is " + dynamic_variable[0].title())  #Tuhain object-ng 0r utgiig text-d oruulaad hevlej bna.
print("My age is " + str(dynamic_variable[1]))
print("I am adult. It is " + str(dynamic_variable[2]))
print(dynamic_variable[1:])  #Ehnii 1-r elementees hoish hevleh
print(dynamic_variable[:1])  #Suuliin 1 element hevleh
print(dynamic_variable[-1:]) #Suuleesee 1 deh elementees hoish hevleh
MAX_VALUE=5000
print(MAX_VALUE)
x, y, z = 1, 2, 3
print(str(x) + "\n" + str(y) + "\n" + str(z))
balance = 1_000_000
print(str(balance) + "\n")

age = f"My age is {dynamic_variable[1]}"  #Text deer tuhain object-g nemj oruulj bn.
print(age)


#Addition task
print("Additional task")

program_language = ['C', 'C++', 'C#', 'Java', 'Javascript', 'Python', 'PHP', 'HTML', 'CSS']
my_study = f"I am learning {program_language[5].upper()} language."
print(my_study)


#Object-n utgiig oorchloh, nemeh
cars = []  # Hooson utgatai object gargaj baina
print(cars)
cars.append('LC200')  #LC200 utgiig hooson object deer nemj oruulj bna.
print(cars)
cars.append('Harrier')  #Append ni Harrier utgiig cars object-n ard nemj oruulna
print(cars)
cars.append('Prius')
print(cars)
cars.insert(0, 'Sai')  #Cars object-n 0 index deer Sai utgiig nemj baina
print(cars)

#Object-n utgiig ustgah
del cars[0]  #Cars object-n 0r utgiig ustgana
print(cars)
poplist = cars.pop()  #Cars object-n suuliin 1 deh utgiig salgaad poplist huvisagchid hadgalna
print(cars)  #Suuliin 1 deh utga ustgagdsanaar hevlene
print(poplist)  #Suuliin 1 deh utgiig hadgalsnaar hevlene
cars.remove('LC200')  #Object dotroos LC200 gesen utgiig ustgana
print(cars)


##Next tasks
print("Next tasks")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.sort(reverse=False)
print(cars)
cars.reverse()
print(cars)


##Task 2.7
print("\n\nTask 2.7")
towns = []
towns.append('Las Vegas')
towns.append('Bali')
towns.append('Paris')
towns.append('London')
towns.insert(0, 'Dubai')
print("Towns = " + str(towns))
sorted(towns)
print("Towns = " + str(towns))
sorted(towns, reverse=True)
print("Towns = " + str(towns))
towns.reverse()  ##Tuhain daraalliig esregeer ni hevlene. Sort shig usgiin daraallaar hiihgui
print("Towns = " + str(towns))
towns.sort()  ##Usgiin daraallaar erembelne
print("Towns = " + str(towns))
towns.sort(reverse=True)  ##Usgiin esreg daraallaar erembelne. Reverse-s yalgaatai ni usgiin esreg daraalliig ashiglana
print("Towns = " + str(towns))


##Task 2.9
print("\n\nTask 2.9")

mine = []
mine.append('mongolia');
mine.append('ulaanbaatar')
mine.append('city')
mine.insert(0, 'earth')
print(mine[0].title())
print(mine[1].lower())
print(mine[2].upper())
print(f"My {mine[-1]} is {mine[1].title()}, {str(mine[-2]).upper()}\n\t is located in the {mine[0].lower()}")
del mine[0]
print(mine)
mine.reverse()
print(mine)
mine.sort()
print(mine)
mine.sort(reverse=True)
print(mine)
length = len(mine)
print(length)
popped = mine.pop()
popped = "{}{}".format('    Popped value is ', popped)
print(popped)
print(popped.strip())
population = 7_000_000_000
x, y, z = 1, 3, 9
print(f"Earth population is {population}. And earth is one of the {z} planets as well as there is {x} sun. Earth is {y}th planet of sun system.")