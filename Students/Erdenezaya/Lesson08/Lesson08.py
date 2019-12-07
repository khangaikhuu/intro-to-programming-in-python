# Unit tests

def get_formatted_name(firs, last):
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
