from tkinter import *
from functools import partial # To prevent unwanted windows

import random

if __name__ == '__main__':
    class MathTitle:
        def __init__(self, parent):

            # Gui to get numbers and choose type of math
            self.start_frame = Frame(padx=10,  pady=10)
            self.start_frame.grid()

            # Set up number to decide what radio button is selected
            self.var = IntVar()
            self.var.set(0)

            self.low_number = IntVar()
            self.high_number = IntVar()

            # Math Heading heading row 1
            self.math_quiz_label = Label(self.start_frame, text="Math Game Quiz", font="Arial 20 bold")
            self.math_quiz_label.grid(row=1)

            # Entry box, Button & Error Label (row 2)
            self.number_frame = Frame(self.start_frame, width=200)
            self.number_frame.grid(row=2)

            # Lowest number Label, Entry box, and error label
            self.lowest_number = Label(self.number_frame, text="Lowest Number", font="Arial 14")
            self.lowest_number.grid(row=0, column=0, padx=15, pady=5)

            self.number_low = Entry(self.number_frame, font="Arial 19 bold",
                                    width=5)
            self.number_low.grid(row=1, column=0, padx=15, pady=5)

            self.number_low_error = Label(self.number_frame, font="Arial 14", text="")
            self.number_low_error.grid(row=2, column=0, padx=15, pady=5)

            # Highest number Entry box, and error label
            self.highest_number = Label(self.number_frame, text="Highest Number", font="Arial 14")
            self.highest_number.grid(row=0, column=1, padx=15, pady=5)

            self.number_high = Entry(self.number_frame, font="Arial 19 bold",
                                     width=5)
            self.number_high.grid(row=1, column=1, padx=15, pady=5)

            self.number_high_error = Label(self.number_frame, font="Arial 14", text="")
            self.number_high_error.grid(row=2, column=1, padx=15, pady=5)

            # Radio Button Frame, Label, Buttons and Error Label
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

            # Radio button error label
            self.var_error_label = Label(self.radio_frame)
            self.var_error_label.grid(row=5, padx=15, pady=5)

            # Frame for the Buttons
            self.stats_frame = Frame(self.start_frame, padx=10, pady=10)
            self.stats_frame.grid(row=4)

            # help button (row 2)
            self.help_button = Button(self.stats_frame, text="Help",
                                      font=("Arial", "14"),
                                      padx=10, pady=-10, command=self.help, width=10)
            self.help_button.grid(row=0, column=1, padx=10)

            # continue button (row 1)
            self.continue_button = Button(self.stats_frame, text="Continue",
                                       font=("Arial", "14"),
                                       padx=10, pady=-10, width=10, command=self.check_input)
            self.continue_button.grid(row=0, column=2)

            # Quit Button
            self.quit_button = Button(self.start_frame, text="Quit", fg="white",
                                      bg="#660000", font="Arial 15 bold",
                                      command=self.to_quit, padx=10, pady=5, width=5)
            self.quit_button.grid(row=5, pady=5)

        def help(self):
            get_help = Help(self)

        def check_input(self):
            # set low number, high number, and find which radio button was chosen
            low_number = self.number_low.get()
            high_number = self.number_high.get()
            has_errors = "no"
            var = self.var.get()

            try:
                # Check Low number is not a Decimal and Does not have letters and is not blank
                low_number = int(low_number)

                # Check Low number is more than -1000
                if low_number < -1000:
                    self.number_low_error.config(text="Can not be less"
                                                      "\n"
                                                      "than -1000")
                    self.number_low.config(bg="#ffafaf")
                    has_errors = "yes"

                # Check Low number is less than 1000
                elif low_number > 1000:
                    self.number_low_error.config(text="Can not be more"
                                                      "\n"
                                                      "than 1000")
                    self.number_low.config(bg="#ffafaf")
                    has_errors = "yes"

                else:
                    # set error message below low number to blank, and set the colour of the entry box to normal
                    self.number_low_error.config(text="")
                    self.number_low.config(bg="SystemButtonFace")
                    try:
                        # Check High number is not a Decimal and Does not have letters and is not blank
                        high_number = int(high_number)

                        # Check high number is more than -1000
                        if high_number < -1000:
                            self.number_high_error.config(text="Can not be less"
                                                               "\n"
                                                               "than -1000")
                            self.number_high.config(bg="#ffafaf")
                            has_errors = "yes"

                        # Check High number is less than 1000
                        elif high_number > 1000:
                            self.number_high_error.config(text="Can not be more"
                                                               "\n"
                                                               "than 1000")
                            self.number_high.config(bg="#ffafaf")
                            has_errors = "yes"

                        # check high number is more than low number
                        elif high_number < low_number:
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

                        # Check high number and low number are not the same
                        elif high_number == low_number:
                            self.number_high_error.config(text="Numbers can \n"
                                                               "not be the same")
                            self.number_high.config(bg="#ffafaf")
                            self.number_low_error.config(text="Numbers can \n"
                                                              "not be the same")
                            self.number_low.config(bg="#ffafaf")
                            has_errors = "yes"


                        else:
                            self.number_high_error.config(text="")
                            self.number_high.config(bg="SystemButtonFace")
                            has_errors = "no"

                            # Check that a radio button has been selected
                            if var == 0:
                                self.var_error_label.config(text="Please choose one of the above.", font="Arial 14")
                                has_errors = "yes"

                    except ValueError:
                        self.number_high_error.config(text="Enter a Whole Number")
                        self.number_high.config(bg="#ffafaf")
                        has_errors = "yes"

            except ValueError:
                self.number_low_error.config(text="Enter a Whole Number")
                self.number_low.config(bg="#ffafaf")
                has_errors = "yes"

            # Continue if there are no issues
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
                  "Once you have chosen your numbers, select addition, " \
                  "subtraction, multiplication or division." \
                  "\n\n" \
                  "Then press Continue to move on to the next part."

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

        # Record actual answer, question number, questions answered and correctly answered
        # Set the correct answer up to be an intiger
        self.true_answer = IntVar()
        self.true_answer.set(0)
        # Set the question number up to be an intiger, and set it to 0, as it will be updated on
        # question generation
        self.question_number = IntVar()
        self.question_number.set(o)
        # Set the questions answered up to be an intiger, and set to 0, as none have been answered yet
        self.questions_answered = IntVar()
        self.questions_answered.set(0)
        # Set the questions answered correctly up to be an intiger, and set to 0, as none have been answered correctly yet
        self.correctly_answered = IntVar()
        self.correctly_answered.set(0)
        # used to remember the buttons enabled and disabled before stats is opened
        self.bach = IntVar()

        # Create a blank List to store all questions and answers
        self.all_calculations = []

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        #if user press cross instead of dismiss, close help and release help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_game, partner))

        # set up gui frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        self.number_frame = Frame(self.help_frame, width=300)
        self.number_frame.grid(row=0)

        # Set up the numbers to be recorded for the stats all_calculations list
        self.num1_rec = IntVar()
        self.num2_rec = IntVar()

        # set question number
        self.how_heading = Label(self.number_frame, text="Question {}:".format(self.question_number.get()),
                                 font="Arial 15", width=10, anchor=W)
        self.how_heading.grid(row=1, column=0, padx=5)

        # show the question
        self.first_number = Label(self.number_frame, text="{}", font="Arial 15", anchor=W)
        self.first_number.grid(row=1, column=1)

        self.symbol = Label(self.number_frame, text="{}", font="Arial 15", anchor=W)
        self.symbol.grid(row=1, column=2)

        self.second_number = Label(self.number_frame, text="{}", font="Arial 15", anchor=W, width=12)
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
                                      command=partial(self.check_answer, partner))
        self.answer_question.grid(row=0, column=0, pady=15)

        # help button (row 2)
        self.help_button = Button(self.lower_frame, text="Help", font="Arial 14", command=self.help2, width=10)
        self.help_button.grid(row=1, column=0, pady=15)

        # continue button
        self.continue_button = Button(self.lower_frame, text="Continue", font="Arial 14", width=10,
                                      command=partial(self.next_question, partner))
        self.continue_button.grid(row=0, column=1, pady=15, padx=2)
        self.continue_button.config(state=DISABLED)

        # dismiss button (row 2)
        self.stats_button = Button(self.lower_frame, text="Stats", width=10,
                                  bg="#660000", font="Arial 14 bold", fg="white",
                                  command=lambda: self.open_stats(self.all_calculations))
        self.stats_button.grid(row=1, column=1, pady=15, padx=2)

        # set up a variable to record what buttons are enabled or disabled when closing stats. works by
        # setting as 0 or 1, which will either enable or disabled the continue or submit button when closing stats box.
        self.bach = IntVar()

        # generate questions from the next_question function
        self.next_question(partner)

    # disable buttons when opening stats
    def open_stats(self, calc_history):

        # disable all buttons in game class
        self.continue_button.config(state=DISABLED)
        self.stats_button.config(state=DISABLED)
        self.help_button.config(state=DISABLED)
        self.answer_question.config(state=DISABLED)
        # carry over stats list to stats box
        Stats(self, calc_history)

    # Close everything
    def close_game(self, partner):
        root.destroy()

    #open help
    def help2(self):
        get_help = Help2(self)

    # checks answer is correct
    def check_answer(self, partner):

        # grab variable to check answer, and add to stats list
        # Grab correct answer to check against user answer
        answer = self.true_answer.get()
        # Grab user answer to check against correct answer
        user_answer = self.answer_entry.get()
        #gets the number of questions answered to increase by 1 if there are no errors
        questions_answered = self.questions_answered.get()
        #grab numbers used in question to record for stats
        num1 = self.num1_rec.get()
        num2 = self.num2_rec.get()
        # Grab variable used for first radio buttons
        math_variable = partner.var.get()
        # grab how many have been answered correctly so far, to update if needed
        correctly_answered = self.correctly_answered.get()

        # op_text used in this case to add the correct variable to the stats function
        if math_variable == 1:
            op_text = "+"

        elif math_variable == 2:
            op_text = "-"

        elif math_variable == 3:
            op_text = "×"

        else:
            op_text = "÷"

        # Check if user answer is correct, incorrect or a value error
        try:
            # checks if user answer is a number.
            user_answer = int(user_answer)
            answer = int(answer)

            # checks answer is correct
            if user_answer == answer:
                self.answer_entry.config(bg="#3DCE30")
                self.entry_error_label.config(text="Correct", fg="green")
                # sets bach to 1, so that when the buttons update, if the user decides to open
                # stats, it will enable the correct buttons when closing stats
                bach = 1
                self.bach.set(bach)
                # edits buttons so user cannot answer the same question twice
                self.answer_question.config(state=DISABLED)
                self.continue_button.config(state=NORMAL)
                # updates the questions answered for the stats at the end
                questions_answered = questions_answered + 1
                self.questions_answered.set(questions_answered)
                # puts the question number, question and user answer in the list marked correctly
                question_summary = "Q{}:  {} {} {} = {} - Correct".format(questions_answered, num1, op_text, num2,
                                                                          user_answer)
                self.all_calculations.append(question_summary)
                # updates correctly_ answered questions number for end stats
                correctly_answered = correctly_answered + 1
                self.correctly_answered.set(correctly_answered)

            # function for if user gets the answer inccorect
            else:
                self.entry_error_label.config(text="Incorrect", fg="red")

                # Change entry box background to pink
                self.answer_entry.config(bg="#ffafaf")
                # edits buttons so user cannot answer the same question twice
                self.answer_question.config(state=DISABLED)
                self.continue_button.config(state=NORMAL)
                # sets bach to 1, so that when the buttons update, if the user decides to open
                # stats, it will enable the correct buttons when closing stats
                bach = 1
                self.bach.set(bach)
                # updates the questions answered for the stats at the end
                questions_answered = questions_answered + 1
                self.questions_answered.set(questions_answered)
                # puts the question number, question, user answer and the correct answer in the list marked incorrectly
                question_summary = "Q{}.  {} {} {} = {} - Incorrect: Answer = {}".format(questions_answered,
                                                                                         num1, op_text,
                                                                                         num2, user_answer, answer)
                self.all_calculations.append(question_summary)

        # if the user answers with anything but a number
        except ValueError:
            # error telling user numbers only
            self.entry_error_label.config(text="Numbers Only")

            # Change entry box background to pink
            self.answer_entry.config(bg="#ffafaf")
            # set bach to 0, so that if the user opens then closes stats, continue button is still disabled
            bach = 0
            self.bach.set(bach)

    # generate next question
    def next_question(self, partner):

        # set bach to 0, to remember that the continue button is now disabled
        self.bach.set(0)

        # set variables used to develop questions
        # grabs the variable used, addition, multiplication, subtraction, division
        math_variable = partner.var.get()
        # Get the low number from the User input at the start
        low_number = partner.low_number.get()
        # Get the high number from the User input at the start
        high_number = partner.high_number.get()

        # edit question number
        question_number = self.question_number.get()
        question_number = question_number + 1
        self.question_number.set(question_number)

        # generate new random numbers
        num1 = random.randint(low_number, high_number)
        num2 = random.randint(low_number, high_number)
        # set these variables as new numbers for stats list purposes
        self.num1_rec.set(num1)
        self.num2_rec.set(num2)

        # generate next question
        # op_text used to update the question, so users dont have to remember thier chosen radio button.
        if math_variable == 1:
            op_text = "+"
            # caluclates answer by adding num1 and num 2
            answer = num1 + num2

        elif math_variable == 2:
            op_text = "-"
            # caluclates answer by subtracting num1 and num 2
            answer = num1 - num2

        elif math_variable == 3:
            op_text = "×"
            # caluclates answer by multiplying num1 and num 2
            answer = num1 * num2

        else:
            op_text = "÷"
            # caluclates answer by multiplying num1 and num 2 to get num3, setting num1 as the
            # answer, and then setting num3 as num1, making it so the answer is always an initger
            num3 = num1 * num2
            answer = num1
            num1 = num3

        # set the true answer for answer hecking purposes
        self.true_answer.set(answer)

        # edit the question that appears on screen
        self.first_number.config(text="{}".format(num1))

        self.symbol.config(text="{}".format(op_text))

        self.second_number.config(text="{}".format(num2))

        # set buttons to normal
        self.answer_question.config(state=NORMAL)
        self.continue_button.config(state=DISABLED)
        self.entry_error_label.config(text="")
        self.answer_entry.config(bg="SystemButtonFace")
        self.answer_entry.delete(0, 'end')
        # update the question number to be the next question
        self.how_heading.config(text="Question {}:".format(self.question_number.get()))


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


class Stats:
    def __init__(self, partner, calc_history):
        
        # get questions answered and correctly answered to calculate percentage score
        questions_answered = partner.questions_answered.get()
        correctly_answered = partner.correctly_answered.get()
        
        # set up new variables fore easier programming for stats and export
        self.questions_answered = IntVar()
        self.correctly_answered = IntVar()
        self.questions_answered.set(questions_answered)
        self.correctly_answered.set(correctly_answered)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if user press cross instead of dismiss, close stats and release stats button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_stats, partner))

        # set up gui frame
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # set up stat heading (row 0)
        self.how_heading = Label(self.history_frame, text="Game Stats",
                                 font="Arial 16 bold")
        self.how_heading.grid(row=0)

        # stat text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your game "
                                                           "stats. You can use the "
                                                           "export button to save this "
                                                           "data to a text file if "
                                                           "desired.",
                                  font="Arial 12 italic",
                                  justify=LEFT, width=30,
                                  wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 10:
            for item in range(0, 10):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your game "
                                              "stats. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export/dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 14 bold",
                                     command=partial(self.close_stats, partner))
        self.dismiss_button.grid(row=0, column=1)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 14 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # checks if stats are blank, and if stats is blank then disable export button
        if questions_answered == 0:
            self.export_button.config(state=DISABLED)
        else:
            self.export_button.config(state=NORMAL)
        
        # Quit button
        self.finish_btn = Button(self.history_frame, text="Quit",
                                 font="Arial 14 bold", bg="#660000", fg="white", command=partial(self.finish, partner))
        self.finish_btn.grid(row=4)

    # quit function
    def finish(self, partner):
        finish = Finish(self)

    def close_stats(self, partner):
        # get bach for checking which buttons hould be enabled and disabled upon closing stats
        bach = partner.bach.get()

        # checks whether submit button was active or not before opening stats
        if bach == 1:
            partner.continue_button.config(state=NORMAL)
            partner.stats_button.config(state=NORMAL)
            partner.help_button.config(state=NORMAL)
            partner.answer_question.config(state=DISABLED)
            self.history_box.destroy()

        else:
            partner.continue_button.config(state=DISABLED)
            partner.stats_button.config(state=NORMAL)
            partner.help_button.config(state=NORMAL)
            partner.answer_question.config(state=NORMAL)
            self.history_box.destroy()

    # export function
    def export(self, calc_history):
        Export(self, calc_history)


class Finish:
    def __init__(self, partner):
        # disable quit button
        partner.finish_btn.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.finish_box = Toplevel()

        # if user press cross instead of dismiss, close export and release export button
        self.finish_box.protocol('WM_DELETE_WINDOW', partial(self.close_finish, partner))

        # set up gui frame
        self.finish_frame = Frame(self.finish_box)
        self.finish_frame.grid(row=0)

        # ask user for quit confirmation
        self.finish_label = Label(self.finish_frame, text="Would you like to quit?", font="Arial, 18")
        self.finish_label.grid(row=0, pady=5)

        self.button_frame = Frame(self.finish_frame)
        self.button_frame.grid(row=1)

        # yes button
        self.yes_btn = Button(self.button_frame, text="Yes", font="Arial 14", command=partial(self.quit456))
        self.yes_btn.grid(row=0, column=0, padx=5, pady=5)

        # no button
        self.no_btn = Button(self.button_frame, text="No", font="Arial 14", command=partial(self.close_finish, partner))
        self.no_btn.grid(row=0, column=1, padx=5, pady=5)

    def close_finish(self, partner):
        # put export button back to normal
        try:
            self.finish_box.destroy()
            partner.finish_btn.config(state=NORMAL)

        # if user closes stats box before quit box, make sure the porgram doesnt break
        except:
            self.finish_box.destroy()

    #if yes is clicked, close everything
    def quit456(self):
        root.destroy()


class Export:
    def __init__(self, partner, calc_history):

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if user press cross instead of dismiss, close export and release export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # set up gui frame
        self.export_frame = Frame(self.export_box)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export and Instructions",
                                 font="Arial 16 bold")
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text=" Enter a filename in the box below "
                                      "and press the save button to save your "
                                      "Game Stats to a text file. "
                                      "if the filename you enter below already exists, "
                                      "its contents will be replaced with your Game "
                                      "Stats",
                                 justify=LEFT, width=40,
                                 wrap=225, padx=10, pady=10, font="Arial 12")
        self.export_text.grid(row=2, pady=10)

        # error message labels ( initially blank, row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon")
        self.save_error_label.grid(row=4)

        # Save / Cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", font="Arial14",
                                    command=partial(self.close_export, partner), width=10)
        self.cancel_button.grid(row=0, column=1, padx=15)

        self.save_button = Button(self.save_cancel_frame, text="Save", font="Arial14",
                                  command=partial(lambda: self.save_history(partner, calc_history)), width=10)
        self.save_button.grid(row=0, column=0, padx=15)

    def save_history(self, partner, calc_history):
        # allowed characters in filename
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        # grabs file name for checking
        filename = self.filename_entry.get()

        # checks for valid characters
        for letter in filename:
            if re.match(valid_char, letter):
                continue

            # error if space is used
            elif letter == " ":
                problem = "(no spaces allowed)"
            # error if punctuation used
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"

        # error if filename is blank
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error msg
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")

        # update stats with final info for exporting to a text file
        else:
            # grab questions answered and correctly answered from stats, which were grabbed from game
            questions_answered = partner.questions_answered.get()
            correctly_answered = partner.correctly_answered.get()

            # claculate precentage
            percentage = correctly_answered / questions_answered
            percentage = percentage * 100

            # round to 2 decimal places
            percentage = float("{:.2f}".format(percentage))

            # add .txt suffix!
            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at the end of each item
            for item in calc_history:
                f.write(item + "\n")

            # generates a message based on how well you do, based on precentage score
            f.write("\n\nYou Answered {} Correctly out "
                    "of {}".format(correctly_answered, questions_answered))
            if percentage == 100:
                f.write(" - You got all the questions correct, Well Done.")

            elif percentage >= 80:
                f.write(" - You got {}% of the questions correct, Good Job.".format(percentage))

            elif percentage >= 50:
                f.write(" - You got {}% of the questions correct, Not Bad.".format(percentage))

            elif percentage >= 20:
                f.write(" - You got {}% of the questions correct, Practise Some More.".format(percentage))

            elif percentage >= 10:
                f.write(" - You got {}% of the questions correct, At least it wasn't 0".format(percentage))

            elif percentage == 0:
                f.write(" - You got {}% of the questions correct, Ouch.".format(percentage))

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal
        try:
            partner.export_button.config(state=NORMAL)
            self.export_box.destroy()

        # close export even if stats was already closed
        except:
            self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Game")
    something = MathTitle(root)
    root.resizable(False, False)
    root.mainloop()
