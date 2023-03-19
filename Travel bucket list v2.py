import easygui as e

def duping():

    dupe_list = []
    for place in place_list:
        if place_list.count(place) > 1 and place not in dupe_list:
            dupe_list.append(place)
            e.msgbox("Please do not enter a duplicate")
    return

while True:
    place = e.enterbox("Enter the name of five place you would "
                             "like to visit separated by a comma")
    place_list = place.split(",")
    if len(place_list) > 5 or len(place_list) < 5:
        e.msgbox(f"You entered {len(place_list)} Please enter 5 names")

    e.msgbox(f"My bucket list:\n- {place_list[0]}\n- {place_list[1]}"
                   f"\n- {place_list[2]}\n- {place_list[3]}\n- {place_list[4]}")
    
    dupper = duping()

    e.enterbox("Enter the new place")




