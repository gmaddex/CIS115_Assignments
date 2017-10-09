#Gabe Maddex
#CIS 115 Scholars Section
#This program emulates a game of pick up sticks against another player or AI
from random import randint
sticks_remaining = 20
counter = 0

print("Welcome to Pick up Sticks!")
print("Would you like to play against the computer, or by yourself like a strange, lonely little child?")
game_option = input("(C)omputer or (Y)ourself: ")

if game_option == 'Y' or game_option == 'y':
    while sticks_remaining > 0:
        #draws stick
        for i in range(0,6):
            for i in range(0,sticks_remaining):
                print("|  ", end='')
            print("\n")
        #prints number below, adjusting for number length
        for i in range(0,sticks_remaining):
            if i < 9:
                print(str(i + 1) + "  ", end='')
            else:
                print(str(i + 1) + " ", end='')
        #player 1 turn set to false automatically, changes when on aneven numbered turn
        player1_turn = False
        if counter % 2 == 0:
            player1_turn = True
        if player1_turn:
            print("\nPlayer 1's turn.")
        else:
            print("\nPlayer 2's turn.")
        #sets remaining number of sticks equal to input as an int
        takes = int(input("Would you like to take 1, 2, or 3 sticks? "))
        sticks_remaining -= takes
        print("Player takes " + str(takes) + " stick(s). " + str(sticks_remaining) + " remaining.")
        counter += 1

    if sticks_remaining <= 0:
        if player1_turn:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

if game_option == 'C' or game_option == 'c':
    while sticks_remaining > 0:
        #draws stick
        for i in range(0,6):
            for i in range(0,sticks_remaining):
                print("|  ", end='')
            print("\n")
        #prints number below, adjusting for number length
        for i in range(0,sticks_remaining):
            if i < 9:
                print(str(i + 1) + "  ", end='')
            else:
                print(str(i + 1) + " ", end='')
        #player 1 turn set to false automatically, changes when on an even numbered turn
        player1_turn = False
        if counter % 2 == 0:
            player1_turn = True
        if player1_turn:
            print("\nPlayer 1's turn.")
            #sets remaining number of sticks equal to input as an int
            takes = int(input("Would you like to take 1, 2, or 3 sticks? "))
            sticks_remaining -= takes
            print("Player takes " + str(takes) + " stick(s). " + str(sticks_remaining) + " remaining.")
        else:
            print("\nPlayer 2's turn.")
            #Computer draws a random number of sticks, so long as at least that number of sticks remains.
            if sticks_remaining > 3:
                takes = randint(1,3)
            else:
                takes = randint(1, sticks_remaining)
            sticks_remaining -= takes
            print("Player 2 takes " + str(takes) + " stick(s). " + str(sticks_remaining) + " remaining.")
        counter += 1

    if sticks_remaining <= 0:
        if player1_turn:
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")


