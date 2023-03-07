import easygui
import random

win = 0
lose = 0
while True:
    weapons = ["Paper", "Scissors", "Rocks"]
    computer = random.choice(weapons)
    play_again = easygui.buttonbox("Welcome to Rock, Paper, Scissors\n\n"
                                   "Rock beats scissors\n"
                                   "Scissors beats papr\n "
                                   "Paper beats rock\n"
                                   "Do you want to play?\n"
                                   "Welcome and Rules", choices=["Yes", "No"])
    if play_again == "No":
        break
    else:
        player = easygui.buttonbox("Choose your weapon", "Choose weapon",
                                   choices=[weapons[0], weapons[1], weapons[2]])
        easygui.msgbox(f"You choose {player} and the computer "
                       f"chose {computer}", "Choice")
        if computer == player:
            result = "This was a draw"
        elif computer == "Paper" and player == "Scissors" or computer == \
            "Scissors" and player == "Paper" or \
            computer == "Rock" and player == "Scissors":

            result = "You lose"
            lose += 1
        else:
            result = "You win"
            win += 1
        print(lose + win)

        easygui.msgbox(result)
        if win != 0:
            percentage = win / (lose + win)
            easygui.msgbox(f"You have {percentage* 100}% win rate")
        else:
            easygui.msgbox("Your trash")
print("GG ")
