import sys
import os
import random
choice = random.randint(1, 2)
import time
a=2
b=0.08
player_health = 30


def print_slow(str, delay = 0.1):   #This is for the delay between dialogue. I wish for the player to steadily follow whats' going on in the game.
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def reset_console():              #In case a glitch occurs during the game, I have set up a reset point on whatever section the player was previously in so they can continue with the narrative.
        print("\n")
        os.system('cls_clear')

def fprint( str, delay = 0):
            print("\n")
            time.sleep(delay)

def sprint(str,delay=0):     #This speeds up certain dialogue, like a random quick time event for example.
    print(str)
    time.sleep(delay)

def entrance():
    print(" The cavern-Created by Student 1915233")
    p1 = "\nYou and your family decided to go out on a hike, but due to your curiousity and hubris you are now trapped in a dark cave. The entrance has been sealed off by fallen boulders as you entered. \nyou either had to run in or get crushed by the incoming debris. \n........\nThere is no way out. \nYou decide to walk on and see what you can find, hopefully find another entrance or exit you can use to reunite with your family... they don't even know where you are as of now."
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    b1="\nJust Ahead, you can barely see a cavern. this is the only other means of travel, there are no other entrances. \nWill you continue?"
    for character in b1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    while True:
        action = input("\n>")
        if action == "yes":
            cavern()
        elif action == "no":

            print("A bat flies over your head,you also hear screeches in the distance")
            time.sleep(2)
            print("Do you decide to move on?")
            time.sleep(2)
        else:

            print("you sit in total darkness, wondering if there's a way out.")
            time.sleep(2)
            print("perhaps now is the time to go?")

        # the use of\n allows dialogue to space out and not look messy, it helps the player stay on track.


def cavern():
    global player_health                                   # Global health ties to how much damage the player can take before the game ends. Unfortunetly the idea for proper combat was scrapped due to conflicting code and me not being able to locate a fix in time. I will learn from this.
    bat_attack = random.choice([True,False])
    if bat_attack == True:
        print("You were suddenly attacked by a bat! The screeches you heard from before signalled their arrival")
        player_health -= random.randint(1,15)
        if player_health < 29:
            print("The bat managed to strike a decent blow! You are now wounded")


    g1="You then proceed to stumble into a dimly lit cavern. There is a small crevice near the ceiling that lets a flow of light into the cave. \nYou are thankful. \n You begin to survey the area and discover two things."    # instead of using print, I add different key names for sentences so they can have different load speeds than one of another, some dialogue moves across the screen faster than others depending on the situation.
    for character in g1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    h1="\nYou cannot go right or left, however the cave seems to continue forward,the cave seems to extend endlessly but your source of light seems to end just as the cavern begins to enlarge. \nWill you press on?"
    for character in h1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    while True:
        action = input("\n>")
        if action == "yes":
            Hallway()
        elif action == "no":
            k1="You decide to sit down and think about what to do,You enjoy being able to see your surroundings but due to how large the cave is that appears to not be a lasting feeling. \nPerhaps going forward will be your best bet in order to find a way out of here."
            for character in k1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.023)
            time.sleep(2)
            print("\ndo you decide to leave?")

        else:
            print("The cold is getting to you. You proceed to shiver due to how cold it is, perhaps it is time to leave?.")


def Hallway():
    t1="You can't see anything, you merely feel your way around your surroundings, this hallway seems to go on indefinitely. You move your hands around what feels to be a wall and trust in your footing with each step you take, But the lack of vision makes this more difficult than it has to be."
    for character in t1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)

    n1="\nYou stand still and lament on what to do, Your vision is practically null and void, you can't rely on your sight anymore. \ndo you press on into the dark? what dangers could be lurking in the shadows. The looming fear of the unknown begins to envelop you. there's nowhere else to go."
    for character in n1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    time.sleep(2)
    d1="\nWhat do you do? do you move on and see where luck takes you? or do you stand idly by and wait for something to happen?"
    for character in d1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    while True:
        action = input("\n>")
        if action == "yes":
            pit()
        elif action == "no":
           m1= "You sit down and ponder. You want to be back home with your family, the isolation is getting to you. But you can't give up now, not when there's stil a chance to get out of here and get back home!"
           for character in m1:
               sys.stdout.write(character)
               sys.stdout.flush()
               time.sleep(0.023)
               l1="\n...You have to keep it together"
        for character in l1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.023)
        else:
            time.sleep(2)
            j1="\nWhat was that? it sounded like a scream. it almost sounded human, who else can be in this cave? \nDo you attempt to leave?"
            for character in j1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.023)


def pit():

    s1= "You lose your footing and fall into a an ominous and languid pit, you lay there in a complete daze. Due to the fact that you couldn't see where you were going you have now fallen even further into the cave. \n....things are looking grim."
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)



    p1="Your back took the brunt of that fall, it could've been worse but that's beside the point. You're now in an even worse situation than you were previously in. \nYour vision begins to blur.."
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    k1="You can try to climb out, but the fall was pretty vast. And with your battered back climbing will be tedious. \n You slowly lift yourself back up with what little strength you have left and look up. With a stirn grin think about what to do. \n Do you attempt to climb up?"
    for character in k1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    while True:
        action = input("\n>")
        if action == "yes":
            h1="As You gather your strength and begin to walk towards a side of the pit you believe you can climb. It is slightly arched towards the right so if you're able to get halfway up you can begin to lean on the wall. \n  You have to think about your injuries however. \nAs you attempt to climb out, you can almost see a clearing but you lose grip on what you were once holding onto and fall back down again. \n As you lie there, you begin to feel your strength leave you. You close your eyes slowly...."
            time.sleep(3)
            game_over()
            for character in h1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.023)
        elif action == "no":

         v1 = "As you lay there, you begin to realise how dire this situation is. No one is around to help you and you are surrounded by darkness, Hopelessness begins to set in."
        for character in v1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.023)





def game_over():

    print(''' 
    
    
MM'"""""`MM MMP"""""""MM M"""""`'"""`YM MM""""""""`M    MMP"""""YMM M""MMMMM""M MM""""""""`M MM"""""""`MM 
M' .mmm. `M M' .mmmm  MM M  mm.  mm.  M MM  mmmmmmmM    M' .mmm. `M M  MMMMM  M MM  mmmmmmmM MM  mmmm,  M 
M  MMMMMMMM M         `M M  MMM  MMM  M M`      MMMM    M  MMMMM  M M  MMMMP  M M`      MMMM M'        .M 
M  MMM   `M M  MMMMM  MM M  MMM  MMM  M MM  MMMMMMMM    M  MMMMM  M M  MMMM' .M MM  MMMMMMMM MM  MMMb. "M 
M. `MMM' .M M  MMMMM  MM M  MMM  MMM  M MM  MMMMMMMM    M. `MMM' .M M  MMP' .MM MM  MMMMMMMM MM  MMMMM  M 
MM.     .MM M  MMMMM  MM M  MMM  MMM  M MM        .M    MMb     dMM M     .dMMM MM        .M MM  MMMMM  M 
MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMMMM MMMMMMMMMMMM    MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMM MMMMMMMMMMMM                                                                                                        
    ''')


entrance()


