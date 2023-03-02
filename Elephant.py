import easygui
import random

word = "elephant"

for i in range(5):
    letter = random.choice(word)
    easygui.msgbox(letter, f"Letter {i+1} chosen")


