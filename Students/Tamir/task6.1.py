from random import randint as r

print("\nTask 6.1")

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(r(1, self.sides))


die1 = Die()
die1.roll_die()
die2 = Die(12)
die2.roll_die()