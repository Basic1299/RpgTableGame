import random
import Cube
import Arena
import Mage
import Warrior
import Warlock
import os
import time
import Thief

sixCube = Cube.Cube()


def char_pick():
    loop = True
    while loop:
        print("Classes: Warrior(1)  Mage(2)  Warlock(3)  Thief(4)")
        print("----------------------------")
        pick = input("Pick the class\n>")
        os.system('clear')
        if pick == "1":
            return "1"
        elif pick == "2":
            return "2"
        elif pick == "3":
            return "3"
        elif pick == "4":
            return "4"


def char_decision(name, pick):
    if pick == "1":
        return Warrior.Warrior(name, sixCube)
    elif pick == "2":
        return Mage.Mage(name, sixCube)
    elif pick == "3":
        return Warlock.Warlock(name, sixCube)
    elif pick == "4":
        return Thief.Thief(name, sixCube)


def name_pick(player):
    print(f"---{player}---")
    p2name = input("Choose your name\n>")
    os.system('clear')
    return p2name


play = "yes"
while play == "yes":
    # Name and class picking
    print("Welcome to the battle arena!")
    p1 = char_decision(name_pick("Player 1"), char_pick())
    name = name_pick("Player 2")
    while name == p1.name:
        input("You cannot pick the same name like your opponent!")
        os.system('clear')
        name = name_pick("Player 2")
    p2 = char_decision(name, char_pick())
    while p1.char == p2.char:
        input("You cannot pick the same class like your opponent!")
        os.system('clear')
        p2 = char_decision(name, char_pick())
    input("Let the game begin!\nPress enter for continue...")

    game = Arena.Arena(p1, p2)

    # Random start
    if random.randint(0, 1):
        (p1, p2) = (p2, p1)

    # game loop
    loop = 1
    while not game.is_over():
        os.system('clear')
        if not game.is_over():
            game.round(p1, p2, loop)
        else:
            break
        input("Press enter to continue...")

        os.system('clear')
        if not game.is_over():
            game.round(p2, p1, loop)
        else:
            break
        input("Press enter to continue...")
        loop += 1

    # show finish results
    os.system('clear')
    print("-----------------------")
    print(f"{game.looser()} died.")
    print(f"{game.winner()} has won the battle!")
    print("-----------------------")
    play = input("Do you wanna play again? (yes/no)\n>")
    os.system('clear')






























