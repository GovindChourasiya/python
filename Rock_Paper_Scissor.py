# .....Its a game that can be played between two persons, in which they have to give their actions
# at same interval of time together by means of some hand gestures implying Rock,Paper and Scissor.
# The rules of the game are very simple, as we know that rock can break the scissor ,similarly scissor
# can cut the paper , and also paper can be wrapped around a rock covering it as a whole.
# Hence, when rock and scissor are in the ground then rock will win, likewise in case of scissor and 
# paper scissor will win and at last with rock and paper paper will win .
# Also if both the players shows the same gesture either rock, paper or scissor then the game would 
# be tied....... 
# Here we've been playing this game with computer.

import random as r
# importing random functions helps the computer to make choices randomly

while True:
    User_Input = input("Enter a choice (rock, paper, scissors): ")
    Type_of_choices = ["rock", "paper", "scissors"]
    computer_choice = r.choice(Type_of_choices)
    print("\nYou choose",User_Input,"computer choose",computer_choice,"\n")

    if User_Input == computer_choice:
        print("Both players selected",User_Input,"It's a tie!")
    elif User_Input == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif User_Input == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif User_Input == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
    
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input(" Do you want to Play again?\n (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing the Game :)")
    
        break
  