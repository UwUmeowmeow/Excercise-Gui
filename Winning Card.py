import random as r
from easygui import *


cards = ["two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "Jack", "Queen", "King", "Ace"]

suits = ["clubs", "diamond", "hearts", "spades"]

while True:

    Computer = r.choice(cards)
    Computer_suit = r.choice(suits)
    Player = r.choice(cards)
    Player_suits = r.choice(suits)

    if cards.index(Computer) > cards.index(Player):
        game_1 = buttonbox(msg=f"You draw {Player} {Player_suits} and Computer draw "
                               f"{Computer} {Computer_suit} lost", title="Game Result",
                           choices=["exit", "play again"])
        if game_1 == "exit":
            exit()

    elif cards.index(Computer) < cards.index(Player):
        game_2 = buttonbox(msg=f"You draw {Player} {Player_suits}and Computer draw "
                               f"{Computer} {Computer_suit} you Won", title="Game Result",
                           choices=["exit", "play again"])
        if game_2 == "exit":
            exit()

