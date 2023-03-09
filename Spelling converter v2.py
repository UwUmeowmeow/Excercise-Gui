import easygui

while True:

    first_input = easygui.enterbox("Please enter the NZ word", "Word to check")
    word = first_input
    word = word.replace("s", "z")
    word = word.replace("u", "")
    if word == first_input:
        easygui.msgbox("No change in spelling")
    else:
        easygui.msgbox(f"The American spelling of [{first_input}] is [{word}]", "Result")
    game = easygui.buttonbox(choices=["Exit", "Enter new NZ word"])
    if game == "Exit":
        exit()
