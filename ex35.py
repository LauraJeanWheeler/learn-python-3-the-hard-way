# note: I did not finish copying the program
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn how to type a number")
    if how_much < 50:
        print("Nice, you're not too greedy, you win!")
        exit(0)
    else: 
        dead("You are greedy!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

# While True means loop forever
# until something within the loop returns or breaks.
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you then slaps your face")
       

def dead(why):
    print(why, "Good job!")
    exit(0)