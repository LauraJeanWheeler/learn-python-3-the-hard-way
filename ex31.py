print("""You enter a dark room with two rats
      Do you pet rat #1 or rat #2?""")

door = input("> ")

if door == "1":
    print("The rat is grey, cute, and is eating a peice of pie.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the rat")
    rat = input("> ")

    if rat == "1":
        print("The rat eats your face off.")
    elif rat == "2":
        print("The rat ets your legs off.")
    else:
        print("Well doing {rat} is probably better...")
        print("The rat runs away (rattily)")

if door == "2":
    print("The white rat is jumping on a ball.")
    print("What do you do?")
    print("1. Turn on BOB get amp up the M00D")
    print("2. Start jumping on the ball with the rat")
    rat = input("> ")

    if rat == "1" or rat == "2":
        print("You sure know how to have fun!")
        print("Good job :)")
    else:
        print("You are a bigger buzzkill than will.i.am")

else:
    print("You do not care for rats and they do not care for you.")
    print("They eat your eyeballs in a fit of passion.")