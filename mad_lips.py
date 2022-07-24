"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
"""

print('Please enter the following words:\n')
adjective = input('Adjective: ')
animal = input('Animal: ')
verb1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('verb: ')

#Creating the story
print('\nYour story is as it follows:\n')
print('The other day, I was really in trouble. It all started when',
'I saw a very', adjective.lower(), animal.lower(), verb1.lower(),
f'{exclamation.capitalize()}!', 'I yelled. But all I could think to do',
'was to', verb2.lower(), 'over and over. Miraculously, that caused it',
'to stop, but not before it tried to', verb3.lower(), 'in front'
'of my family.\n')

# The extra mile
print('And now, you can create chapter two to your story!\n')
food = input('Food: ')
onomatopoeia = input('Onomatopoeia: ')
print('\nChapter Two:\n')
print('After the', animal.lower(), 'left, we tried to call it',
'back with some', food.lower(), f'The {animal.lower()} returned',
'and exclaimed:', f'{onomatopoeia.upper()}!.')
print('THE END\n--------------------------------')