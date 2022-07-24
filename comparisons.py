# Comparing numbers
first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))
if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')
if first_number == second_number:
    print('The numbers are equals')
else:
    print('The numbers are not equals')
if first_number < second_number:
    print('The second number is greater')
else:
    print('The second number is not greater')

# Comparing strings
print()
fav_animal = input('What is your favorite animal? ')
if fav_animal.lower() == 'tardigrade':
    print("That's my favorite animal too!")
else:
    print("That's not my favorite animal")