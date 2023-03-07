import easygui


while True:
    place = easygui.enterbox("Enter the name of five place you would "
                             "like to visit separated by a comma")
    place_list = place.split(",")
    if len(place_list) > 5 or len(place_list) < 5:
        easygui.msgbox(f"You entered {len(place_list)} Please enter 5 names")

    easygui.msgbox(f"My bucket list:\n- {place_list[0]}\n- {place_list[1]}"
                   f"\n- {place_list[2]}\n- {place_list[3]}\n- {place_list[4]}")
