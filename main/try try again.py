#Resources:
#https://codereview.stackexchange.com/questions/237601/simple-python-turn-based-battle-game
#https://stackoverflow.com/questions/63534191/developing-a-turn-based-battle-game
#from playsound import playsound

from enum import Enum
import sys
import time
import tkinter as tk
import random

#i tried importing code from another file but it dont work for me :/
#so enjoy function dump

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
            if "N" in temp.upper(): #contains Y and not N
                print("Please enter a valid value: Y or N")
                continue
            return 1
        elif "N" in temp.upper():
            if "Y" in temp.upper(): #contains N and not Y
                print("Please enter a valid value: Y or N")
                continue
            return 0
        else: #either both or neither n or y
            print("Please enter a valid value: Y or N")
            continue

def dly(): #random delay
    time.sleep(random.randint(3,5)/2) #1.5 - 2.5 secs

def ldly(): #random delay 2: electric boogaloo
    time.sleep(random.randint(8,14)/2) #4 - 7 secs


#end of func dump

print("""
\\\\\\\\\\\\\\\\\\\\

shitty game v0.2 No copyright @ your mother 2023
where did you even get this

-------
Disclaimer: Game dialogue can be mildly offensive to some players and includes curse words. 
By continuing to play this game, you accept that you will not complain about getting offended by anything in it.
Type in either (A)ccept to start or (D)ecline to automatically exit.
-------""")

#see nut for disclaimer code DO NOT FORGET DEBUG PURPOSES ONLY {UNCOMMENT}

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

#input() {UNCOMMENT}

#######

#class chr(): (idek)

#def distance(km): enable choosing between miles and km in lore (implement later)

#######
 
def game():

    #print(">You're an adventurer unknown to these lands. You came to find a artifact that is not coded in this version of the game. ")
    
    dly()
    print('>You wake up.\n>This isn\'t your bed.')
    time.sleep(3)
    print('''\n>There\'s a fish floating in your peripheral vision. You slowly sit up and stare at it.''')
    dly()
    print('whatthefuck.jpeg ')
    dly()
    print('''>"Hey, you. You’re finally awake. You were trying to cross the border, right? Walked right into that ambush."''')
    time.sleep(4)
    print('''>Probably not a threat.
>You decide to ignore it for now and inspect your surroundings.
>Your enchanted pack is lying next to you on the ground.
>You turn your gaze to yourself.
>You have a mint green hoodie and some dark blue trousers on. You're a bit hurt, but there are some bandages on your visible wounds.''')
    time.sleep(4)
    print('''
>Satisfied with your inner monologue, you turn to the discount Paimon.
>Its derpy face portrays no emotions, though its foot long body bobs up and down in the air. Probably magic.
>"Are you alright? Do you have brain damage?"
How will you respond?
    'Who are you?' [1]
    'What are you?' [2]''')

    input()
    ldly()
    print('''>"I guess you really do have brain damage," it sighs.
Do you remember anything about yourself? What's your name?"''')
    
    while(True): #silly easter egg
        name = input("Enter character name: ")
        if name.upper() == ("NO"):
            print("Your name is 'Nameless'?")
            if playerY() == 0:
                print("Sure.")
                continue
            else:
                print("Weird name, but okay.")
                name = 'Nameless'
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
    
    print('"I\'m '+name+'," you respond.\n>"It seems you\'ve retained some of your memory. That\'s good."') 
    dly() #i'm so sorry whoever reads this code
    print('>"I\'m Bob, the Sacabambaspis guide you hired when you came to Placeholder. We were travelling to a small town named Dublin when we got attacked by a flock of geese."') 
    print('''>"We\'re currently about 50 kilometers from any people, so I had to make do with the first aid we packed."
>You stand up and brush yourself off. The barren landscape here is a bit dry, so there's quite a bit of dust on you.''')
    print('>You notice Bob air-swimming around your leather backpack.')
    dly()
    print('>"I was barely able to chase the birds off last time without your help, so they\'re probably coming back for more.\nCould you lend me a hand this time?"')
    ldly()
    print('"Sure."')
    dly()
    print('''>You walk to your bag and inspect your [Inventory].
(There should be a new window popping up right about now.)''')
    #inventory()
    print('''>Bob swims down(?) to inspect the items you have in there.
>Health potions, some rations, and a dull sword. There should also be some starter crafting materials, but the crafting system hasn't been coded yet.
>You equip the Dull Blade.


''')




   # (This is the fighting tutorial. Do you want to learn how to fight? This won't affect the story.")''')

    if playerY() == 0:
        print("You won or something! Congratulations on beating up some birds. You got placeholder XP!")

    print('''>After a short break, you and your trusty sea creature companion set off on an uneventful journey to your destination in the middle of bumfuck nowhere.
>You
          
          
          
          
          
          
          
          
          
          
          
''')
        







game()

        
