import easygui

used_tech = easygui.enterbox("Enter the days on which you used tech\n"
                             "separate each day with a space",
                             "Day tech was used")

days = len(used_tech.split())
if days <= 3:
    easygui.msgbox(f"Congratulations. You had {days} tech days with"
                   f" {7-days} tech-free days", "Goal achieved")

else:
    easygui.msgbox(f"Too bad. You used tech on {7-days} tech free days\n"
                   f"That is {days-3} less than your goal.", "Goal failed")
