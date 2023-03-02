import easygui
import random

player = 0

for roll in range(1, 3):
    player += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    easygui.msgbox(f"Player {roll}\nrolled {dice1}"
                   f"\nand {dice2}\nTotal {dice1 + dice2}")
