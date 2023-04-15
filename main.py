# Made by Marcouscous!
# Only support python3

# Import required modules used by the program (so it can operate properly)
import random
import sys
import os

# Board values! Modify these to safely change the way the program looks!
borderChar = "⬜️"
emptyChar = "⬛️"
playerChar = "👽"
portalChar = "🚀"
rows = 5
columns = 5

# This clears the screen to look nicer
os.system('cls' if os.name == 'nt' else 'clear')

# This calculates the total amount of squares the board should have
totalSquares = rows * columns


# This sets the default position of the player and the end-goal.
# By default, it randomly sets it. To hardcode it, it must apply to these rules:
#
# 1. It's value cannot be under 1.
# 2. It's value cannot be over the total amount of squares
#
# Failing to comply with these rules will result in your player/portal not being rendered!


player = random.randint(1, totalSquares)
portal = random.randint(1, totalSquares)


# If the portal and the player are located at the same place, move the portal away!
if portal == player:
    portal += 1



# This block of code renders the entire game. There is no need to modify it.
# To safely make changes to it, use the Board Values at the top of the file!!
def render():
    os.system('cls' if os.name == 'nt' else 'clear')


    if player == portal:
        print("YOU WIN!")
        sys.exit()



    print()
    print("Type up, left, right or down to control your player.")
    print(f"Your objective is to get to the {portalChar}. You are the {playerChar}")
    print("Input your command below.\n")

    squares = 0

    for b in range(rows + 2):
        print(borderChar, end=" ")

    print()

    for i in range(columns):
        print(borderChar, end=" ")
        for j in range(rows):
            
            squares += 1
            if squares == player:
                print(playerChar, end=" ")
                
            elif squares == portal:
                print(portalChar, end=" ")
            else:
                print(emptyChar, end=" ")
               
        print(borderChar, end=" ")
        print()

    for c in range(rows + 2):
        print(borderChar, end=" ")

    print()



# This block of code handles input.
# Modifying the names of the commands is safe, but modifying anything else may make the game unplayable!

while True:
    render()
    q = input("Command: ")

    q = q.lower()
    if q == "down":
        if player + rows > totalSquares:
            print("Error: Cannot move down")
        else:
            player += rows
    elif q == "up":
        if player - rows < 1:
            print("Error: Cannot move up")
        else:
            player -= rows
    elif q == "left":
        if player - 1 < 1:
            print("Error: Cannot go left")
        else:
            player -= 1
    elif q == "right":
        if player + 1 > totalSquares:
            print("Error: Cannot go right")
        else:
            player += 1
    else:
        print("Not a valid command")
    print()