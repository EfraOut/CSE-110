#Efrain Arturo Gomez 
#Auto-grader API

#Main Function.
def main():
	grade = float(input('What is your grade? '))
	finalGrade = gradePicker(grade)
	print(f'your grade is: {finalGrade}')

#Funtion that grades automaticly given the note in numbers.
def gradePicker(grade):
	if grade >= 90:
		return('A')
	elif grade >= 80:
		return('B')
	elif grade >= 70:
		return('C')
	elif grade >= 60:
		return('D')
	else:
		return('F')

#Start of the Aplication
main()