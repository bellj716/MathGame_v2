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
            self.help_button = Button(self.start_frame, text="Continue", font="Arial 12", command=self.first_question)
            self.help_button.grid(row=2, pady=10)

        def first_question(self):
            get_help = Game(self)

class Game:
    def __init__(self, partner):

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

        thingy = random.randint(1, 4)

        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)

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

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        self.number_frame = Frame(self.help_frame, width=300)
        self.number_frame.grid(row=0)

        # set question number
        self.how_heading = Label(self.number_frame, text="Question {}:".format(self.question_number.get()),
                                 font="Arial 15", width=10, anchor=W)
        self.how_heading.grid(row=1, column=0, padx=5)

        # show the question
        self.first_number = Label(self.number_frame, text="{}".format(num1), font="Arial 15", anchor=W)
        self.first_number.grid(row=1, column=1)

        self.symbol = Label(self.number_frame, text="{}".format(op_text), font="Arial 15", anchor=W)
        self.symbol.grid(row=1, column=2)

        self.second_number = Label(self.number_frame, text="{}".format(num2), font="Arial 15", anchor=W, width=12)
        self.second_number.grid(row=1, column=3)

        # frame for answering question
        self.entry_box_frame = Frame(self.help_frame, width=300)
        self.entry_box_frame.grid(row=1)

        # Space for answering the question and error when answering
        self.answer_entry = Entry(self.entry_box_frame, font="Arial 15", width=10)
        self.answer_entry.grid(row=1, column=0, pady=5, padx=15)

        self.entry_error_label = Label(self.entry_box_frame, text="", font="Arial 15")
        self.entry_error_label.grid(row=2, column=0, pady=5)

        # Frame for buttons
        self.lower_frame = Frame(self.help_frame, width=10)
        self.lower_frame.grid(row=5)

        # Submit button
        self.answer_question = Button(self.lower_frame, font="Arial 15", text="Submit", width=10,
                                      command=partial(self.check_answer))
        self.answer_question.grid(row=0, column=0, pady=15)

        # help button (row 2)
        self.help_button = Button(self.lower_frame, text="Help", font="Arial 14", command=self.help2, width=10)
        self.help_button.grid(row=1, column=0, pady=15)

        # continue button
        self.continue_button = Button(self.lower_frame, text="Continue", font="Arial 14", width=10,
                                      command=partial(self.next_question))
        self.continue_button.grid(row=0, column=1, pady=15, padx=2)
        self.continue_button.config(state=DISABLED)

        # dismiss button (row 2)
        self.dismiss_btn = Button(self.lower_frame, text="Stats", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white")
        self.dismiss_btn.grid(row=1, column=1, pady=15, padx=2)

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

    def next_question(self):

        question_number = self.question_number.get()
        question_number = question_number + 1
        self.question_number.set(question_number)

        thingy = random.randint(1, 4)

        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)

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
    root.mainloop()
