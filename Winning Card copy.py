import easygui
import random


dice_roll = []


for times in range(1,6):    
    dice_roll.append(random.randint(0,6))

print(dice_roll)
most = []
for hi in range(1,7):
    print(f"Number of {hi} rolled: {dice_roll.count(hi)}")
    if dice_roll.count(hi) >= 3:
        most = [hi, dice_roll.count(hi)]
print(f"Most: {most}")