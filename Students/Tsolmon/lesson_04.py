my_info = {'first_name':'Tsolmon', 'last_name':'Yadmaa','city':'Ulaanbaatar'}
print(my_info['first_name'])

river = {'tuul':'Mongolia', 'nile':'Egypt','amazon':'brazil'}
for rivers, country in river.items():
    print(f"The {rivers.title()} runs through {country.title()}")
