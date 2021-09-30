"""
Author: Efrain Gomez Fajardo
Purpose: Asking the user some questions and displaying them back
"""
def main():
    color = input('Please type your favourite colour:\n')
    print('Your favourite colour is ' + color +'\nInteresting choice')
    # Asking something else, for the extra mile
    onomatopoeia = input('Now, for something more interesting, tell me your favourite onomatopoeia:\n')
    print(onomatopoeia + ' is a very funny onomatopoeia!')
main()