from tkinter import *
from functools import partial # To prevent unwanted windows

import random

if __name__ == '__main__':
    class MathTitle:
        def __init__(self, parent):

            # Gui to get numbers and choose type of math
            self.start_frame = Frame(padx=10,  pady=10)
            self.start_frame.grid()

            # Myath Heading heading row 1
            self.mystery_box_label = Label(self.start_frame, text="Math Game Quiz", font="Arial 20 bold")
            self.mystery_box_label.grid(row=1)

            #help button (row 2)
            self.help_button = Button(self.start_frame, text="Continue", font="Arial 12", command=self.help)
            self.help_button.grid(row=2, pady=10)

        def help(self):
            get_help = Game(self)

class Game:
    def __init__(self, partner):

        #disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if user press cross instead of dismiss, close help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        self.score_frame = Frame(self.help_frame, width=300)
        self.score_frame.grid(row=0)

        # set up help heading (row 0)
        self.how_heading = Label(self.score_frame, text="Question: 1/10",
                                 font="Arial 10", anchor=E, width=50)
        self.how_heading.grid(row=0)

        self.number_frame = Frame(self.help_frame,width=300)
        self.number_frame.grid(row=1)

        self.first_number = Label(self.number_frame, text="1", font="Arial 15")
        self.first_number.grid(row=1, column=0)

        self.symbol = Label(self.number_frame, text="+", font="Arial 15")
        self.symbol.grid(row=1, column=2)

        self.second_number = Label(self.number_frame, text="1", font="Arial 15")
        self.second_number.grid(row=1, column=3)

        self.answer = Entry(self.help_frame, font="Arial 15", width=10)
        self.answer.grid(row=2, pady=5)

        self.answer_question = Button(self.help_frame, font="Arial 15", text="Submit", width=10)
        self.answer_question.grid(row=3, pady=10)

        self.lower_frame = Frame(self.help_frame, width=10)
        self.lower_frame.grid(row=4)

        # help button (row 2)
        self.help_button = Button(self.lower_frame, text="Help", font="Arial 14", command=self.help2, width=10)
        self.help_button.grid(row=0, column=0, padx=10, pady=15)

        self.help_button = Button(self.lower_frame, text="Continue", font="Arial 14", width=10)
        self.help_button.grid(row=0, column=1, padx=10, pady=15)

        #dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Finish", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=5, pady=10)

    def close_help(self, partner):
        root.destroy()

    def help2(self):
        get_help = Help2(self)


class Help2:
    def __init__(self, partner):

        #disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if user press cross instead of dismiss, close help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help2, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        #set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help and Instructions",
                                 font="Arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="The program will generate a question using numbers " \
                  "in between the 2 numbers you chose at the start." \
                  "\n\n" \
                  "Input the answer into the box and press Enter or click the " \
                  "submit button." \
                  "\n\n" \
                  "The box will turn green if you are correct, " \
                  "and red if you are incorrect." \
                  "\n\n" \
                  "Then press continue to move onto the next question or press " \
                  "Finish to end the game and go to your results early."

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        #dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=partial(self.close_help2, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help2(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = MathTitle(root)
    root.mainloop()
