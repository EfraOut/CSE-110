""""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Combining strings with numbers
"""

age = input('How old are you? ')
next_age = int(age) + 1
print(f'On your next birthday you will be {next_age}\n')

cartons = int(input('How many cartons of eggs do you have? '))
eggs = cartons * 12
print(f'You have {eggs} eggs\n')

cookies = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))
print(f'Each person may have {cookies / people} cookies\n')