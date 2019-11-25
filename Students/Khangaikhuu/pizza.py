
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    print(toppings)
    for topping in toppings:
        print(f"- {topping}")



toppings = ['Cheese', 'Zaidsan Delbeet', 'Test', 'Test']

for i in toppings:
    make_pizza(10, i)