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

# binary search 