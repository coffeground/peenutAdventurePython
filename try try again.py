#Resources:
#https://codereview.stackexchange.com/questions/237601/simple-python-turn-based-battle-game
#from playsound import playsound

from enum import Enum
import sys
import time



print("""
\\\\\\\\\\\\\\\\\\\\

shitty game v0.1 No copyright @ your mother 2023
where did you even get this

-------
Disclaimer: Game dialogue can be mildly offensive to some players and includes curse words. 
By continuing to play this game, you accept that you will not complain about getting offended by anything in it.
Type in 'ACCEPT' to start, or 'DECLINE' to close the game.
-------""")

while(True):
    temp = input().upper()
    if temp == "ACCEPT":
        break
    elif temp == "DECLINE":
        print("Okay. The program will exit in 10 seconds.")
        time.sleep(10)
        sys.exit()
        break
    else:
        print("Please type either 'ACCEPT' or 'DECLINE'.")
        continue

print(""" 
      
///////////      

This is a text-based game. You type in things the game tells you to.

Objects of interest are mostly surrounded in straight brackets: "[]"

Example:
    Blah blah blah
    Option 1 [1]
    Option 2 [2]
    Option 3 [3]

In this situation, you are free to choose from 1 to 3. Type in the selected number: enter '2' without the quotation marks, for example.
(Putting in a + or - sign returns an error.)

I hope you understand, but if you don't there's no function to see this text again unless you restart the entire game.
Good luck, i guess.

///////////

(Press enter to continue with the game)

    """)

input()

#######

#class chr():

#def distance(lng): enable choosing between miles and km in lore

def playerChoose(lastOption): #choose between 1 and unspecified last option, returns option number, asks again when entered anything else
    while(True):
        try:
            temp = int(input())
            if temp <= lastOption:
                return temp
            else:
                continue
        except:
            print("Please enter a number between 1 and "+lastOption+".")
            continue

def playerY(): #asks player for yes or no, returns 1 if string contains 'y', 0 if it contains 'n', tries again if it contains both
    while(True): #its stupid but i dont know about any edge cases that cause problems so ill pretend they dont exist
        temp = input("[Y/N] ")
        if "Y" in temp.upper():
            if "N" in temp.upper():
                print("Please enter a valid value: Y or N")
                continue
            return 1
        elif "N" in temp.upper():
            if "Y" in temp.upper():
                print("Please enter a valid value: Y or N")
                continue
            return 0
        else:
            print("Please enter a valid value: Y or N")
            continue

#######
 
def game():


    print(""">You wake up.
>This isn't your bed.

>There's a fish floating in your peripheral vision. 
whatthefuck.jpeg 
>Probably not a threat. You ignore it for now and inspect your surroundings.
>You're in a field of wheat. There's nothing of note for miles.
>Your leather pack is lying next to you on the ground. It probably came with you when whatever force transported you here.
>You turn your gaze to yourself.
>As far as you can tell, you don't have any injuries.
>You have a mint green sweater and some dark blue trousers on.


>Satisfied with your inner monologue, you turn to the discount Paimon.
>"Hey, you. You’re finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there."
>You're sure it was quoting something, but you're not sure. You examine the fish fo
>Its derpy face portrays no emotions, though its foot long body slowly bobs up and down in the air. Probably magic.
How will you respond?
    'Who are you?' [1]
    'What are you?' [2]""")

    input()

    print('''>"I'm Bob, the guide you hired when you came to the land of Placeholder.
Do you remember anything about yourself? What's your name?"''')
    
    while(True): #silly easter egg
        name = input("Enter character name: ")
        if name.upper() == ("YES"):
            print("Your name is 'What'?")
            if playerY() == 0:
                print("I can see why.")
                continue
            else:
                print("Weird name, but okay.")
                break
        
        temp = sum(not chr.isspace() for chr in name)
        if temp > 40:
            print("Please enter a  name shorter than 40 characters.")
        elif temp < 1:
            print("Names cannot be blank.")
            continue
        print("Your name is",name+"? Are you sure?")
        if playerY() == 0:
            continue
        else:
            break
    
    print('>"Okay, '+name+'. I\'m glad to see you back. We were going to a town named Dublin when we got attacked by a flock of geese."')
    print('''>"We\'re currently about 50 kilometers from any people, so I had to make do with the first aid we packed."
>You stand up and brush yourself off. The dirt around here is a bit dry, so there's quite a bit of dust on you.

    




    (This is the fighting tutorial. Do you want to learn how to fight? This won't affect the story.")''')

    if playerY() == 0:
        print("You won or something! Congratulations on beating up some birds. You got placeholder XP!")
    else:
        fight()







game()

        
