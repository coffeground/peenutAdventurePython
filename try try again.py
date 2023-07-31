import playsound


print("""
\\\\\\\\\\\\\\\\\\\\

shitty game v0.1 No copyright @ your mother 2023
where did you even get this

-------
Disclaimer: Game dialogue can be mildly offensive and includes cuss words. By playing this game, you accept that you have fully read the Terms and Conditions of using this software.
-------

This is a text-based game. You mostly type in numbers that correspond to the options on the screen.
You can examine your inventory and items in it by typing "INV" and "INSPECT" respectively.

Objects of interest are mostly surrounded in straight brackets: "[]"
Options that are enclosed in curly brackets "{}" advance the story, and you cannot go back after selecting them.

Example:
    Blah blah blah
    Option 1 [1]
    Option 2 [2]
    {Option 3} [3]

In this situation, you are free to choose from 1 to 3, though it is recommended that you try both 1 and 2 before proceeding.
(Putting in a + or - sign returns an error.)

I hope you understand, but if you don't there's no function to see this text again unless you restart the entire game.
Good luck, i guess.

\\\\\\\\\\\\\\\\\\\\\

(Press enter to continue with the game)

    """)

input()

#######

def fight():

def playerChoose(lastOption): #choose between 1 and unspecified last option, returns option number, asks again when entered anything else
    while(True):
        try:
            temp = int(input())
            if temp <= lastOption:
                return temp
            else:
                continue
        except:
            print("Please enter a number between 1 and",lastOption,".")
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
>You ignore it for now and inspect your surroundings.
>You're in a field of wheat. There's nothing of note for miles.
>Your leather pack is lying next to you on the ground. It probably came with you when whatever force transported you here.
>You turn your gaze to yourself.
>As far as you can tell, you don't have any injuries.
>You have a mint green sweater and some dark blue trousers on.
>The ground around you is a bit dry, so they aren't too dirty. You brush off some dust.

>Satisfied with your inner monologue, you turn to the discount Paimon.
"Hey, you. You’re finally awake. You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there."
>You don't see anyone in your vicinity that the fish could be referring to. You look back at the thing.
>Its derpy face portrays no emotions, though its foot long body slowly bobs up and down in the air. Probably magic.
How will you respond?
    'Who are you?' [1]
    'What are you?' [2]""")

    input()

    print(""""Sacabambaspis like myself are fairly common in the land of Placeholder. I am Bob, your guide in these lands.
Do you remember anything about yourself?"
What is your name?""")
    
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
    
    print(""""It seems you have not lost all of your memory. You were knocked unconscious when a flock of geese ganged up on you.
    I tried to fend them off, but it seems they're coming back to finish the job. Look out!"
    (This is the fighting tutorial. Do you want to learn how to fight? This won't affect the story.")""")

    if playerY() == 0:
        print("You won or something! Congratulations on beating up some birds. You got placeholder XP!")
    else:
        fight()








#    playsound('https://youtu.be/YOuMxmzmxqk')
        
game()

        
