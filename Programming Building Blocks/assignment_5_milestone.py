"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Adventure Game (practice if statements)
"""
print('--' * 40)
print("Hero's Journey\nGame inspired by Joseph Campbell's 'Hero's Journey'")
print('--' * 40)
print("it's a normal day in life, nothing too special. Except there is something special.\nYou can feel the calling.\nYou accept the calling ")
print("\nYou head outside, not knowing what awaits for you. You find on your path a sword and a bow with arrows.\nYou somehow know that you can't take both.")
weapon = input("Which one will you take? Sword/Bow\n")
if weapon.lower() == 'sword':
    print('Even though you have never used it before, you feel confidente.')
    sword = True
    bow = False
elif weapon.lower() == 'bow':
    print('You can feel how your aiming abilities increased just by holding it.')
    bow = True
    sword = False
else:
    print("Well, I guess you're adventuring empty handed.")
    sword = False
    bow = False