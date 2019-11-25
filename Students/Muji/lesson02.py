# Lesson 02 Homework assignment
# ---------------------------------
print("# 1.1")
person='Elon Mask'
print(f"'Hello {person}'' Do you like to fly vehicle to space today? ")
print("'Hello  {} again Do you like to fly vehicle to space today?".format(person))
#-------------------------------------------
print("# 1.2")
print(person.lower())
print(person.upper())
print(person.title())
#-------------------------------------------
print("# 1.3")
quote="I have no special talent, I am anly passionately curios"
author="Albert Einstien"
quote_output=f"{author} once said, '{quote}'."
print(quote_output)
#-------------------------------------------
print("# 1.4")
famous_person="Tomas Edison"
quote_output=f"{famous_person} once said, '{quote}'."
print(quote_output)
#-------------------------------------------
print("# 1.5")
person_name="\tGandi\t"
print(person_name)
print("Prime ministers of India:\nMahatma Gandhi\nIndra Gandhi\nNehru Gandhi")
print("Prime ministers of India: \n\tMahatma Gandhi \n\tIndra Gandhi\n\tNehru Gandhi")
print("lstript() is ", person_name.lstrip())
print("rstript() is ", person_name.rstrip())
print("stript() is ", person_name.strip())
#-------------------------------------------
print("# 2.1")
friends=['Osk', "Tung", "Bek","Buyna"]
print(friends[0])

#-------------------------------------------
print("# 2.2")
transportation=["Toyota Rav4", "Ford unveil SUV", "Tesla X"]
message=f"I am going to buy a {transportation[0]} in 2020"
print(message)


#-------------------------------------------
print("# 2.3")
dinner=['Osk', "Tung", "Bek","Buyna"]
#print(f" I would like to invite you for my GMJ ceremony Dear  {i}" for i in dinner )
print(f"I would like to invite you for my GMJ ceremony Dear {dinner[0:]}. I will happy for you see there. ")


#-------------------------------------------
print("# 2.4")
print(f"Who can't come in dinner is {dinner[-1]}")
dinner[-1]="Warron"
print( "I would like to invite you for my GMJ ceremony Dear {}. I will happy for you see there. ".format(dinner ))

#-------------------------------------------
print("# 2.5")

dinner.insert(0, 'Sarah')
dinner.insert(int(len(dinner)/2), 'Tomas')
dinner.insert(len(dinner), 'Eddison')
print(dinner)
print(f"I would like to invite you for my GMJ ceremony Dear {dinner[0:]}. I will happy for you see there. ")

#-------------------------------------------
print("# 2.6")
print("This time I can only invite two person")
for i in range(len(dinner)-2):
    remove_person=dinner.pop()
    print(f"Dear {remove_person}, I can’t invite you to dinner. I really appolozise this comment ")
print(dinner)

print(f" Dear {dinner[0:]} let me know you your invitation is still valid")
del dinner[0]
print(dinner)
del dinner[0]
print(dinner)

#-------------------------------------------
print("# 2.7")
location_visit=["Hollewood", "Everist", "Huwsgul", "Puji mountain", "Bali"]
print("Original list", location_visit)
location_visit.sort()
print("Sorted list ",location_visit)
location_visit.sort(reverse=True)
print("Reverse sorted list",location_visit)

print("Here is the original list:")
print(location_visit)
print("\nHere is the sorted list:")
print(sorted(location_visit))
print("\nHere is the original list again:")
print(location_visit)
location_visit.reverse()
print(location_visit)


