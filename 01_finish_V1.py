from tkinter import *
from functools import partial # To prevent unwanted windows

import random

if __name__ == '__main__':
    class MathTitle:
        def __init__(self, parent):

            # Gui to get numbers and choose type of math
            self.start_frame = Frame(padx=10,  pady=10)
            self.start_frame.grid()

            self.var = IntVar()
            self.low_number = IntVar()
            self.high_number = IntVar()

            # Math Heading heading row 1
            self.mystery_box_label = Label(self.start_frame, text="Math Game Quiz", font="Arial 20 bold")
            self.mystery_box_label.grid(row=1)

            # Entry box, Button & Error Label (row 2)
            self.number_frame = Frame(self.start_frame, width=200)
            self.number_frame.grid(row=2)

            self.lowest_number = Label(self.number_frame, text="Lowest Number", font="Arial 14")
            self.lowest_number.grid(row=0, column=0, padx=15, pady=5)

            self.lowest_number = Label(self.number_frame, text="Highest Number", font="Arial 14")
            self.lowest_number.grid(row=0, column=1, padx=15, pady=5)

            self.number_low = Entry(self.number_frame, font="Arial 19 bold",
                                    width=5)
            self.number_low.grid(row=1, column=0, padx=15, pady=5)

            self.number_low_error = Label(self.number_frame, font="Arial 14", text="")
            self.number_low_error.grid(row=2, column=0, padx=15, pady=5)

            self.number_high = Entry(self.number_frame, font="Arial 19 bold",
                                     width=5)
            self.number_high.grid(row=1, column=1, padx=15, pady=5)

            self.number_high_error = Label(self.number_frame, font="Arial 14", text="")
            self.number_high_error.grid(row=2, column=1, padx=15, pady=5)

            self.radio_frame = Frame(self.start_frame, padx=10, pady=10)
            self.radio_frame.grid(row=3)

            self.choose_one = Label(self.radio_frame, text="Choose One:", font="Arial 15")
            self.choose_one.grid(row=0, padx=15, pady=5)

            self.addition = Radiobutton(self.radio_frame, text="Addition", font="Arial 12",
                                        variable=self.var, value=1, anchor=W, width=10)
            self.addition.grid(row=1, padx=15, pady=3)

            self.subtraction = Radiobutton(self.radio_frame, text="Subtraction", font="Arial 12",
                                           variable=self.var, value=2, anchor=W, width=10)
            self.subtraction.grid(row=2, padx=15, pady=3)

            self.multiplication = Radiobutton(self.radio_frame, text="Multiplication", font="Arial 12",
                                              variable=self.var, value=3, anchor=W, width=10)
            self.multiplication.grid(row=3, padx=15, pady=3)

            self.division = Radiobutton(self.radio_frame, text="Division", font="Arial 12",
                                        variable=self.var, value=4, anchor=W, width=10)
            self.division.grid(row=4, padx=15, pady=3)

            self.stats_frame = Frame(self.start_frame, padx=10, pady=10)
            self.stats_frame.grid(row=4)

            # help button (row 2)
            self.help_button = Button(self.stats_frame, text="Help",
                                      font=("Arial", "14"),
                                      padx=10, pady=-10, command=self.help, width=10)
            self.help_button.grid(row=0, column=1, padx=10)

            # stats button (row 1)
            self.stats_button = Button(self.stats_frame, text="Continue",
                                       font=("Arial", "14"),
                                       padx=10, pady=-10, width=10, command=self.first_question)
            self.stats_button.grid(row=0, column=2)

            # Quit Button
            self.quit_button = Button(self.start_frame, text="Quit", fg="white",
                                      bg="#660000", font="Arial 15 bold",
                                      command=self.to_quit, padx=10, pady=5, width=5)
            self.quit_button.grid(row=5, pady=5)

        def help(self):
            get_help = Help(self)

        def first_question(self):
            low_number = self.number_low.get()
            high_number = self.number_high.get()
            has_errors = "no"

            try:
                low_number = int(low_number)

                if low_number < -1000:
                    self.number_low_error.config(text="Can not be less"
                                                      "\n"
                                                      "than -1000")
                    self.number_low.config(bg="#ffafaf")
                    has_errors = "yes"

                elif low_number > 1000:
                    self.number_low_error.config(text="Can not be more"
                                                      "\n"
                                                      "than 1000")
                    self.number_low.config(bg="#ffafaf")
                    has_errors = "yes"

                else:
                    has_errors = "no"

            except ValueError:
                self.number_low_error.config(text="Enter a Number")
                self.number_low.config(bg="#ffafaf")
                has_errors = "yes"

            try:
                high_number = int(high_number)

                if high_number < -1000:
                    self.number_high_error.config(text="Can not be less"
                                                       "\n"
                                                       "than -1000")
                    self.number_high.config(bg="#ffafaf")
                    has_errors = "yes"

                elif high_number > 1000:
                    self.number_high_error.config(text="Can not be more"
                                                      "\n"
                                                      "than 1000")
                    self.number_high.config(bg="#ffafaf")
                    has_errors = "yes"
                else:
                    has_errors = "no"

            except ValueError:
                self.number_high_error.config(text="Enter a Number")
                self.number_high.config(bg="#ffafaf")
                has_errors = "yes"

            if high_number < low_number:
                has_errors = "yes"
                self.number_high_error.config(text="Enter a Number"
                                                   "\n"
                                                   " higher than the "
                                                   "\n"
                                                   "lower number")
                self.number_high.config(bg="#ffafaf")
                self.number_low_error.config(text="Enter a Number "
                                                  "\n"
                                                  "lower than the\n"
                                                  " higher number")
                self.number_low.config(bg="#ffafaf")

            if high_number == low_number:
                self.number_high_error.config(text="Numbers can \n"
                                                   "not be the same")
                self.number_high.config(bg="#ffafaf")
                self.number_low_error.config(text="Numbers can \n"
                                                  "not be the same")
                self.number_low.config(bg="#ffafaf")
                has_errors = "yes"

            if has_errors == "no":

                self.high_number.set(high_number)
                self.low_number.set(low_number)

                get_help = Game(self)

                # hide start up window
                root.withdraw()

        def to_quit(self):
            root.destroy()


class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if user press cross instead of dismiss, close help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        #set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help and Instructions",
                                 font="Arial 14 bold")
        self.how_heading.grid(row=0)

        help_text="In the first box enter the lowest number you wish " \
                  "to be used in the quiz. The lowest you can go is -1000." \
                  "\n\n" \
                  "In the second box enter the highest number you wish " \
                  "to be used in the quiz. The highest you can go is 1000." \
                  "\n\n" \
                  "Once you have chosen your numbers"

        # help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        #dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=partial(self.close_help,partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Game:
    def __init__(self, partner):

        thingy = partner.var.get()
        low_number = partner.low_number.get()
        high_number = partner.low_number.get()

        self.true_answer = IntVar()
        self.true_answer.set(0)
        self.question_number = IntVar()
        self.question_number.set(1)

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
        self.how_heading = Label(self.score_frame, text="Question: {}".format(self.question_number.get()),
                                 font="Arial 10", anchor=E, width=50)
        self.how_heading.grid(row=0)

        self.number_frame = Frame(self.help_frame,width=300)
        self.number_frame.grid(row=1)

        num1 = random.randint(low_number, high_number)
        num2 = random.randint(low_number, high_number)

        if thingy == 1:
            op_text = "+"
            answer = num1 + num2

        elif thingy == 2:
            op_text = "-"
            answer = num1 - num2

        elif thingy == 3:
            op_text = "x"
            answer = num1 * num2

        else:
            op_text = "÷"
            num3 = num1 * num2
            answer = num1
            num1 = num3

        self.true_answer.set(answer)

        self.first_number = Label(self.number_frame, text="{}".format(num1), font="Arial 15")
        self.first_number.grid(row=1, column=0)

        self.symbol = Label(self.number_frame, text="{}".format(op_text), font="Arial 15")
        self.symbol.grid(row=1, column=2)

        self.second_number = Label(self.number_frame, text="{}".format(num2), font="Arial 15")
        self.second_number.grid(row=1, column=3)

        self.answer_entry = Entry(self.help_frame, font="Arial 15", width=10)
        self.answer_entry.grid(row=2, pady=5)

        self.entry_error_label = Label(self.help_frame, text="", font="Arial 15")
        self.entry_error_label.grid(row=3, pady=5)

        self.answer_question = Button(self.help_frame, font="Arial 15", text="Submit", width=10,
                                      command=partial(self.check_answer))
        self.answer_question.grid(row=4, pady=10)

        self.lower_frame = Frame(self.help_frame, width=10)
        self.lower_frame.grid(row=5)

        # help button (row 2)
        self.help_button = Button(self.lower_frame, text="Help", font="Arial 14", command=self.help2, width=10)
        self.help_button.grid(row=0, column=0, padx=10, pady=15)

        self.continue_button = Button(self.lower_frame, text="Continue", font="Arial 14", width=10,
                                      command=partial(self.next_question, partner))
        self.continue_button.grid(row=0, column=1, padx=10, pady=15)
        self.continue_button.config(state=DISABLED)

        #dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Finish", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=6, pady=10)

        print(answer)

    def close_help(self, partner):
        root.destroy()

    def help2(self):
        get_help = Help2(self)

    def check_answer(self):

        answer = self.true_answer.get()

        user_answer = self.answer_entry.get()

        try:
            user_answer = int(user_answer)
            answer = int(answer)

            if user_answer == answer:
                self.answer_entry.config(bg="#3DCE30")
                self.entry_error_label.config(text="Correct")
                self.answer_question.config(state=DISABLED)
                self.continue_button.config(state=NORMAL)

            else:
                self.entry_error_label.config(text="Incorrect")

                # Change entry box background to pink
                self.answer_entry.config(bg="#ffafaf")
                self.answer_question.config(state=DISABLED)
                self.continue_button.config(state=NORMAL)

        except ValueError:
            self.entry_error_label.config(text="Numbers Only")

            # Change entry box background to pink
            self.answer_entry.config(bg="#ffafaf")

    def next_question(self, partner):

        low_number = partner.low_number.get()
        high_number = partner.high_number.get()

        question_number = self.question_number.get()
        question_number = question_number + 1
        self.question_number.set(question_number)
        thingy = partner.var.get()

        num1 = random.randint(low_number, high_number)
        num2 = random.randint(low_number, high_number)

        if thingy == 1:
            op_text = "+"
            answer = num1 + num2

        elif thingy == 2:
            op_text = "-"
            answer = num1 - num2

        elif thingy == 3:
            op_text = "x"
            answer = num1 * num2

        else:
            op_text = "÷"
            num3 = num1 * num2
            answer = num1
            num1 = num3

        self.true_answer.set(answer)

        self.first_number.config(text="{}".format(num1))

        self.symbol.config(text="{}".format(op_text))

        self.second_number.config(text="{}".format(num2))

        self.answer_question.config(state=NORMAL)
        self.continue_button.config(state=DISABLED)
        self.entry_error_label.config(text="")
        self.answer_entry.config(bg="SystemButtonFace")
        self.answer_entry.delete(0, 'end')
        self.how_heading.config(text="Question: {}".format(self.question_number.get()))
        print(answer)


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
    root.resizable(False, False)
    root.mainloop()
