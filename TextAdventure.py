import sys
import os
import random
choice = random.randint(1, 2)
import time
a=2
b=0.08



def print_slow(str, delay = 0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def reset_console():
        print("\n")
        os.system('cls_clear')

def fprint( str, delay = 0):
            print("\n")
            time.sleep(delay)

def sprint(str,delay=0):
    print(str)
    time.sleep(delay)

def entrance():
    p1 = "You are in a dark cave. The entry has been sealed by fallen boulders.There is no way out. You decide to walk on and see what you can find."
    for character in p1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    print("\nJust Ahead, you can barely see a cavern. this is the only other means of travel, there are no other entrances. Will you continue?")
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




def cavern():
    g1="You then proceed to stumble into a dimly lit cavern"
    for character in g1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)
    print("\nYou cannot go right or left, however the cave seems to continue forward. Will you press on?")
    while True:
        action = input("\n>")
        if action == "yes":
            Hallway()
        elif action == "no":
            print("You decide to sit down and think about what to do, perhaps going forward will be your best bet.")
            time.sleep(2)
            print("do you decide to leave?")

        else:
            print("The cold is getting to you. You proceed to shiver due to how cold it is")


def Hallway():
    t1="You can't see anything, you merely feel your way around your surroundings, this hallway seems to go on indefinitely"
    for character in t1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.023)

    print("You stand still and lament on what to do, do you press on into the dark? there's nowhere else to go.")
    time.sleep(2)
    print("What do you do? do you move on?")
    while True:
        action = input("\n>")
        if action == "yes":
            pit()
        elif action == "no":
            print("You sit down and ponder. You want to be back home with your family, the isolation is getting to you.")
            time.sleep(2)
            l1=("You have to keep it together")
            for character in l1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.023)
        else:
            print("What was that? it sounded like a scream. it almost sounded human, who else can be in this cave? ")


def pit():
    print(
        "You lose your footing and fall into a an ominous and languid pit, you lay there in a complete daze",
        2)
    sprint("Your back took the brunt of that fall, it could've been worse.",2)
    print("You can try to climb out, but the fall was pretty vast. And with your battered back climbing will be tedious")
    while True:
        action = input("\n>")
        if action == "yes":
            fprint("As you attempt to climb out, you can almost see a clearing but you fall back down again. Damaging your back even further.")
        elif action == "no":
            fprint(
                "As you lay there, you begin to realise how dire this situation is")
        else:
            fprint("You begin to feel hopeless, ")


entrance()


