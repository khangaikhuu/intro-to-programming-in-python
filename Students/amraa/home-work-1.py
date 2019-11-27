# 1.1 
Ner = "amaraa"
print(f"Snu, {Ner.title()}")

# 1.2
name = "Amarjargal"
print(f"{name.title()}, {name.upper()}")

# 1.3

word = "A person who never made a mistake never tried anything new"
print(f"Albert Einstein once said, {word} ")

# 1.4 
person_name = "Albert Einstein"
new_message = "if you can't it simple, you don't understand it well enough"
print(f"{person_name}, {new_message}") 

# 2.1 
names = ["mendee", "odbayar", "bilgvvn"]
print = [names]

# 3.1 
pizza = ["MAXdai pizza", "hawaiy pizza", "engiin pizza"]
for DurtaiPizza in pizza:
    print(f"ene bol minii durtai pizzanuud: {DurtaiPizza.title()}")
print("i love pizza")
# 3.2 
 DurtaiAmitan = ["chono", "nohoi", "baawgai"] 
 for i in   DurtaiAmitan:  
        print(f"minii durtai amitan bol {i.title()}")

# 3.3
x = range(1, 21)
for i in x:
    print(i)
# 3.4
for i in range(1 , 1000001):
    print(i)

# 3.5 
numbers = list(range(1, 1000001))
sum(numbers)
min(numbers)
max(numbers)

# 3.6 
for i in range(1, 21,2):
    print(i)

# 3.7 
for i in range(1, 11):
    i=i*3
    print(i)

# 3.8
for i in range(1, 11):
    i=i**3
    print(i)
# 4.1 
person = {
    'fname': "Amarjargal",
    'lname' : "batchuluun",
    'city' : "erdenet",
    'address': "4-27-14"
}
print(person)

#4.4 
World = {
    "China" : "Tsagaan herem",
    "Mongolia" : "Howsgol",
    "france" : "Tsamhag"
}
for  i in World.keys():
        print(i.title())

for j in World.values():
    print(j.title()) 
    