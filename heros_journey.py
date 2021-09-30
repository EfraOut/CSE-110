"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Adventure Game (practice if statements and decision making)
"""
print('--' * 40)
print("Hero's Journey\nGame inspired by Joseph Campbell's \"Hero's Journey\"")
print('--' * 40)
print("it's a normal day in life, nothing too special. Except there is something special.\nYou can feel the calling.\nYou accept the calling ")
print("\nYou head outside, not knowing what awaits for you. You find on your path a sword and a bow with arrows.\nYou somehow know that you can't take both.")

# Choosing a weapon. Not picking results on leaving empty-handed
weapon = input("Which one will you take? SWORD/BOW\n")
if weapon.lower() == 'sword':
    print("Picking up the sword, you know it can bring protection for your journey.")
    sword = True
    bow = False
elif weapon.lower() == 'bow':
    print('Even though you have never used one, it feels natural for you how to aim and reload at the speed of light.')
    bow = True
    sword = False
else:
    print("That's not a valid option, so you will travel without a weapon")
    sword = False
    bow = False
print("You still don't know what you're supposed to do, but you hope you can figure out while you travel.")

# Wolf encounter. Neither option turns into "run"
print("\nWalking towards the woods, you find a wolf at a moderate distance. He's sleeping.\nAs you try to move away from him you accidentaly kicked a rock. The wolf has awoken.")
decision = input('What do you do? ATTACK/PET/RUN\n')
if decision.lower() == 'attack':
    if sword:
        print("The wolf just stares at you as you unfold your sword and pierce his heart. The light inside his eyes vanishes as you remove the sword from his chest")
    elif bow:
        print("Attack with bow. Wolf is dead")
    else:
        print("Since you didn't grab a weapon, you fist fight. The wolf runs away, meaning not harm to you.")
    wolf_dead = True
    pet = False
    run = False
elif decision.lower() == 'pet':
    print("He's your friend now, and now he's following you")
    wolf_name = input('Name the wolf: ')
    wolf_dead = False
    pet = True
    run = False
elif decision.lower() == 'run':
    print("You were able to escape from the wolf, but apperantly he wasn't a bad wolf anyways.")
    wolf_dead = False
    pet = False
    run = True
else:
    print("Being too late to decide now, your legs force you to run away, outside the woods.")
    wolf_dead = False
    pet = False
    run = True
print("\nLeaving the woods you can see your objective loud and clear. Or at least that's what you thought.")

#Battle with three options. Neither options results in Unsatisfied Ending
print("As you enter your destination, you notice a giant ogre, waiting for you. He's been waiting a long time for this.\nNow your final battle begins!")
battle = input("What do you do? FIGHT/FLEE\n")
if battle.lower() == 'fight':
    if sword and wolf_dead:
        print('Cursed')
        courage = True
    elif sword and run:
        print('Death')
        courage = True
    elif sword and pet:
        print('True')
        courage = True
    elif bow and wolf_dead:
        print('Unstocked')
        courage = True
    elif bow and run:
        print('Solitary')
        courage = True
    elif bow and pet:
        print('Happy')
        courage = True
    elif not sword and not bow and wolf_dead:
        print('One Fist Man')
        courage = True
    elif not sword and not bow and run:
        print("Wendy's")
        courage = True
    elif not sword and not bow and pet:
        print("Murphy's")
        courage = True
    else:
        print('ERROR')
        courage = True
elif battle.lower() == 'flee':
    if sword and wolf_dead:
        print('Coward')
        courage = False
    elif sword and run:
        print('Lazy')
        courage = False
    elif sword and pet:
        print('Un-Analize')
        courage = False
    elif bow and wolf_dead:
        print('Heartless')
        courage = False
    elif bow and run:
        print('Bum')
        courage = False
    elif bow and pet:
        print('Sad')
        courage = False
    elif not sword and not bow and wolf_dead:
        print('Nick Cage')
        courage = False
    elif not sword and not bow and run:
        print('Bad')
        courage = False
    elif not sword and not bow and pet:
        print('Secret')
        courage = False
    else:
        print('ERROR')
        courage = False
else:
    print("Fine. If you don't want to choose, I'll choose for you. And yes, I'm talking to you!")
    courage = True
    wolf_dead = True
    pet = True
    run = True

"""
There are 19 different endings, all conditionals to different actions.
Actions in order:
1. Sword or Bow
2. Attack or Pet or Run wolf (else is Run)
3. Fight or Run (else is Unsatisfied Ending)
"""
print("You can hear a voice. It's a turtle's voice, and it's speaking to you, and it says:\n")
if courage and wolf_dead and run and pet:
    print('Unsatisfied')
    name = 'unsatisfied'
elif sword and wolf_dead and courage:
    print("Cursed")
    name = 'cursed'
elif sword and wolf_dead and not courage:
    print ("Coward")
    name = 'coward'
elif sword and run and courage:
    print("Death")
    name = 'death'
elif sword and run and not courage:
    print("Lazy")
    name = 'lazy'
elif sword and pet and courage:
    print("True")
    name = 'true'
elif sword and pet and not courage:
    print("Un-Analize")
    name = 'un-analyze'
elif bow and pet and courage:
    print("Happy")
    name = 'happy'
elif bow and pet and not courage:
    print("Sad")
    name = 'sad'
elif bow and run and courage:
    print("Solitary")
    name = 'solitary'
elif bow and run and not courage:
    print("Bum")
    name = 'bum'
elif bow and wolf_dead and courage:
    print("Unstocked")
    name = 'unstocked'
elif bow and wolf_dead and not courage:
    print("Heartless")
    name = 'heartless'
elif not bow and not sword and wolf_dead and courage:
    print("One Fist Man")
    name = 'one fist man'
elif not bow and not sword and wolf_dead and not courage:
    print("Nick Cage")
    name = 'nick cage'
elif not bow and not sword and pet and not courage:
    print("Secret")
    name = "secret"
elif not bow and not sword and pet and courage:
    print("Murphy's")
    name = "murphy's"
elif not bow and not sword and run and courage:
    print("Wendy's")
    name = "wendy's"
elif not bow and not sword and run and not courage:
    print("Bad")
    name = 'bad'
else:
    print("You shouldn't be able to see this. If you are reading this, there's a problem")
    name = 'bizzare'

print(f"\nYou just completed the {name.upper()} ENDING!\nWhich other's could you get?\n")
print('--' * 40)
print("\"The cave you fear to enter holds the treasure you seek\" Joseph Campbell")
print("What cave are you afraid of entering, but you know you should enter?")
print('--' * 40)