"""
Purpose: Testing while loops
"""

number = int(input('Please type a positive number: '))

while number < 0:
    print("Sorry, that's an invalid number. Try again")
    number = int(input('Please type a positive number: '))
print(f'Your number is: {number}')

answer = ''
while answer.lower() != 'yes':
    answer = input('May I have a piece of candy? ')
print('Thank you')