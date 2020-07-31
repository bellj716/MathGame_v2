from tkinter import *
from functools import partial # To prevent unwanted windows
import re

import random

class Meh:
    def __init__(self, partner):

        # Formatting variables...
        background_color = "light blue"

        # in actual program this is blank and is populated with calculations.
        self.all_calculations = ['1 + 1 = 2 - Correct',
                                 '1 + 1 = 2 - Correct',
                                 '1 + 1 = 2 - Correct',
                                 '1 + 1 = 2 - Correct',
                                 '1 + 1 = 2 - Correct',
                                 '1 + 1 = 2 - Correct',
                                 '1 + 1 = 2 - Correct',]

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=500, height=700, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature converion heading row 0
        self.temp_converter_label = Label(self.converter_frame, text="Math Game",
                                          font=("Arial", "18", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", "14"),
                                     padx=10, pady=-10,
                                     command=lambda: self.stats(self.all_calculations))
        self.history_button.grid(row=1)

        if len(self.all_calculations) == 0:
            self.history_button.config(state=DISABLED)

    def stats(self, calc_history):
        Stats(self, calc_history)

class Stats:
    def __init__(self, partner, calc_history):

        background = "#a9ef99"  # Pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # sets up child window (ie: history box)
        self.history_box = Toplevel()

        # if user press cross instead of dismiss, close history and release history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # set up gui frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="Arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here is your calculation "
                                                           "history. You can use the "
                                                           "export button to save this "
                                                           "data to a text file if "
                                                           "desired.",
                                  font="Arial 12 italic",
                                  justify=LEFT, width=30, bg=background,
                                  wrap=250, fg="maroon", padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output (row 2)

        # Generate string from list of calculations
        history_string = ""

        if len(calc_history) >= 10:
            for item in range(0, 10):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                              "history. You can use the "
                                              "export button to save this "
                                              "data to a text file if "
                                              "desired.")

        # label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string, bg=background,
                                font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export/dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 14 bold",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 14 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):
        background = "orange"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # sets up child window (ie: export box)
        self.export_box = Toplevel()

        # if user press cross instead of dismiss, close export and release export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # set up gui frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export and Instructions",
                                 font="Arial 16 bold", bg=background)
        self.how_heading.grid(row=0)

        # export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text=" Enter a filename in the box below "
                                      "and press the save button to save your "
                                      "Calculation history to a text file. "
                                      "If the filename you enter below already exists, "
                                      "its contents will be replaced with your calculation "
                                      "History",
                                 justify=LEFT, width=40, bg=background,
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # error message labels ( initially blank, row 3)
        self.filename_entry = Entry(self.export_frame, width=20, font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon", bg=background)
        self.save_error_label.grid(row=4)

        # Save / Cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_cancel_frame)
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

        self.save_button = Button(self.save_cancel_frame, text="save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

    def save_history(self, partner, calc_history):
        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"

        if filename == " ":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            # Display error msg
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        else:
            print("You entered a valid filename")

            # add .txt suffix!
            filename += ".txt"

            # create file to hold data
            f = open(filename, "w+")

            # add new line at the end of each item
            for item in calc_history:
                f.write(item + "\n")

            # close file
            f.close()

            # close dialogue
            self.close_export(partner)

    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Meh(root)
    root.mainloop()
