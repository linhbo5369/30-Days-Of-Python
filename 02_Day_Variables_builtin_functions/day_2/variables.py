# Day 2: 30 Days of python programming
import math

gpa = 10.0
first_name = 'Linh'
last_name = 'Bui'
full_name = first_name + last_name
country = 'Vietnam'
city = 'Ho Chi Minh City'
age = 19
year = 2026
is_married = False
is_true = (age == 19)
is_light_on = True
d, m, y = 17, 10, 2026

print(type(gpa))
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(d))
print(type(m))
print(type(y))
print(f'len(first_name) = {len(first_name)}')
if (len(first_name) < len(last_name)):
    print(f'{first_name} < {last_name}')
elif (len(first_name) > len(last_name)):
    print(f'{first_name} > {last_name}')
else:
    print(f'{first_name} = {last_name}')
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
divison = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_divison = num_one // num_two
radius = 39
# PI = 3.14159
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
radius = int(input('Enter radius of a circle: '))
area_of_circle = math.pi * radius ** 2
print(f'Area of circle: {area_of_circle}')
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter your country: ')
age = int(input('Enter your age: '))
help(tuple)