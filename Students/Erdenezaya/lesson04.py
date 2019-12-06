# lesson_04
alien_0 = {
    'color': 'green',
    'points': 5,
    'x_position': 5.0,
    'y_position': 6.0}
# keys : color, points
# values : green, 5
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green'}
print(alien_0['color'])
alien_0 = {'color': 'green', 'points':5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
# Adding New Key - Value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(f"The alien is {alien_0}.")
#Modifying values in a dictionary
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position':25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
#Move the alien to the right.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#Removing Key-Value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

#Ex - 4.1 
person = {
    'first_name': 'Bat',
    'last_name':'Dorj',
    'age': 25,
    'city': 'Erdenet'}
print(person)

#Ex - 4.2 
favorite_nums = {
    'Naraa': 26,
    'Suvd': 1,
    'Dulguun': 5,
    'Tamir': 4}
print(favorite_nums)
print('Neree oruulna uu:')
input_name = input()
print(f'{input_name}-n durtai toog olooroi')
input_num = input()
num = favorite_nums[input_name]
if input_num == num:
    print('Bayar hurgie!')
else:
    print('taasangui!')
print('Bye!')

#Ex - 4.3

   
    
