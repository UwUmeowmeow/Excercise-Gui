import easygui


def children():
    student_number = easygui.integerbox("What is the maximum number of children "
                                        "allowed per class:"
                                        "\n Must be a number between 10 and 30")
    if student_number > 30 or student_number < 10:
        easygui.msgbox("Invalid number\n"
                       "Please enter a number between 10 and 30")


# Main routine
school = easygui.enterbox("What the name of your school")
children()








