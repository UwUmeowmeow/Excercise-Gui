import easygui

word = easygui.enterbox("Please enter the NZ word", "Word to check")
letters = list(word)
letters.remove("u")
easygui.msgbox(f"The American spelling of {word} is {''.join(letters)}", "Result")
