##FUNCTION
##def gej Function-g zarlana.
##Parameter-r list, integer, string gd buh utgiig damjuulj bolno.

def greeting(x):  ## x ni parameter
    print(f"Hello, {x.upper()}")

guest = input("Guest: ")
greeting(guest) ##guest ni argument


##def pet_animals(type, name, gender = 1): Gender-r yamar 1 argument irehgui bol default-r 1 gesen utga avna
def pet_animals(type, name, gender=1):
    if gender == 0:
        print(f"My female {type} is {name.title()}.")
    elif gender == 1:
        print(f"My male {type} is {name.title()}.")

type = input("Pet type: ")
name = input("Pet name: ")
sex = input("Pet sex: ")
pet_animals(type, name, int(sex))
##Function dahi parameter-n daraalliig medehgui bol parameter, argument 2-g onooj ogch bolno
pet_animals(name=name, gender=int(sex), type=type)
##Gender deer hooson argument ochvol function gender deeree 1 gesen default utgiig avna
pet_animals(type, name, None)


def additional(size=10, *product):
    print(f"Size of {product[0]}")
##product-n urd * tavidag ni producttai ijil torliin heden ch argument ogno bolno gesen ug
additional(None, 'Cheese')


##NULL
##NULL-g Python deer None gej bichdeg.


##IMPORT
##PHP-n include_once -toi ijleer IMPORT command-g ashiglan oor file dotorh function-g duudna
##FROM pizza IMPORT make_pizza - pizza gesen file-s make_pizza gesen function-g duudna
##FROM pizza IMPORT make_pizza as mp - urt function-ii neriig mp bolgoj boginosgono.
    ## mp.



##PYTHON CLASS

#Task 5.1