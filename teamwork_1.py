"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
"""

# Creating the ID
print('Please provide the following information:\n')
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID number: ')
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
month = input('Month of birth: ')
training = input('Completed the training? Y/N: ')
favorite_quote = input('Favorite Quote: ')

# Printing the ID
print("\nThe ID card is:\n---------------------------------")
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title.title())
print('ID: ' + id_number)
print()
print(email_address.lower())
print(phone_number)
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {month.capitalize():14} Training: {training.upper()}')
print(f'Favorite Quote: {favorite_quote.capitalize()}')
print('---------------------------------')