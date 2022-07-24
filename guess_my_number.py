import random

number = random.randint(1, 100)
guess = -1

while guess != number:
    guess = int(input("What's your guess? "))

    if guess < number:
        print('Higher')
    elif guess > number:
        print('Lower')
    else:
        print('You guessed it!')
    