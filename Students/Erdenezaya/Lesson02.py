### Ex 2-3
people = ['Jak Ma', 'Ada Lovelace', 'Adele']
invitation = 'I’d like to invite to dinner. '
print ('Dear ', people[0],",",'\n', invitation)
print ('Dear ', people[1],",",'\n', invitation)
print ('Dear ', people[2],",",'\n', invitation)

### Ex 2-4
people [1] = 'Zuckerberg'
print ('Dear ', people[1],",",'\n', invitation)

### Ex 2-5 
people.append('Dorj')
people.append('Bat')
people.append('Naran')
print ('Dear ', people[3],",",'\n', invitation)
print ('Dear ', people[4],",",'\n', invitation)
print ('Dear ', people[-1],",",'\n', invitation)

### Ex 2-6
print('I can invite only two people for dinner.')
print('Dear ' + people[-1] + ' I am Sorry, I can not invite you to dinner')
people.pop()
print('Dear ' + people[-1] + ' I am Sorry, I can not invite you to dinner')
people.pop()
print('Dear ' + people[-1] + ' I am Sorry, I can not invite you to dinner')
people.pop()
print('Dear ' + people[-1] + ' I am Sorry, I can not invite you to dinner')
people.pop()
print ('Dear ', people[0],",",'\n', invitation)
print ('Dear ', people[-1],",",'\n', invitation)

### Ex 2-7 
places = ['New York', 'Tokyo', 'Paris', 'Berlin', 'Moscow']
print(places)
print(sorted(places))
print(places)
places.sort(reverse=True)
print(places)
places.reverse()
print(places)

### Ex 2-9 
languages = ['Mongolian', 'English', 'Russian', 'Japanese']
print(languages)
languages.append('Korean')
print(languages)
languages.insert(-1,'Chinese')
print(languages)
print(sorted(languages))
languages.reverse()
print(languages)


