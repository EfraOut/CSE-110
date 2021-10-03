from typing_extensions import NotRequired


grade = float(input('What is your grade percentage? '))
note = grade % 10
if grade >= 90:
	letter = 'A'
elif grade >= 80:
	letter = 'B'
elif grade >= 70:
	letter = 'C'
elif grade >= 60:
	letter = 'D'
else:
	letter = 'F'
print(letter)

# Knowing if you passed the class
if grade >= 70:
	print('\nYou passed this course!')
else:
	print('\nNot yet, keep on trying.')