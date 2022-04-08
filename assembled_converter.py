from tkinter import *
from functools import partial
import re
#import random

class Converter:
    def __init__(self,parent):

        #formatting variables
        background_color = "light blue"

        #initialise list to hold calculation history
        self.all_calc_list = []

        #converter frame
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        #temperature converter heading
        self.temp_heading_label = Label(self.converter_frame,
                                        text = "Temperature Converter",
                                            font="Arial 16 bold",
                                            bg=background_color,
                                            padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        #user instructions
        self.temp_instructions_label = Label(self.converter_frame,
                                             text = "Type in the amount to be "
                                                     "converted and then push "
                                                     "one of the buttons below...",
                                                     font="Arial 10 italic", wrap=250,
                                                     justify=LEFT, bg=background_color,
                                                     padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #temperature entry box
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        #conversion buttons frame
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        #answer label
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg = "purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        #history / help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                     text="Calculation History", width=15,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) ==0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"

        #retrive amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            #check and convert to farhenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                farhenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            #check and convert to centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                #invalid input
                answer = "Too cold!"
                has_errors = "yes"

            #display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)
                
            #add answer to list for history
            if has_errors != "yes":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)
            
        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)
            
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded


    def history(self,calc_history):
        History(self,calc_history)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Please enter a number in the box "
                                     "and then push one of the buttons "
                                     "to convert the number to either "
                                     "degress C of degrees F. \n\n"
                                     "The Calculation History area shows "
                                     "up to seven past calculations "
                                     "(most recent at the top). \n\n You can "
                                     "also export your full calculation "
                                     "history to text file if desired.")

class History:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"

        #disable history button
        partner.history_button.config(state=DISABLED)

        #sets up a child window (history box)
        self.history_box=Toplevel()

        self.history_box.protocol('WM_DELETE_WINDOW',partial(self.close_history, partner))

        #set up GUI frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        #set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        #history text (label row1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calcluations. "
                                  "Please use the epxort button to create a text file "
                                  "of all your calculations this session.",
                               font="arial 10 italic", wrap=250,
                                  justify=LEFT, 
                                  fg = "maroon",bg=background,
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        #generate string from list of calculations
        history_string = ""

        if len(calc_history) > 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history) - item - 1]+"\n"
        
        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item)-1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                         "history. You can use the "
                                         "export button to save this "
                                         "data to a text file if "
                                         "desired.")
                                                        
        #label to display calucation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                       font="arial 12", justify=LEFT,bg=background)
        self.calc_label.grid(row=2)

        #export dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        #export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                  font="Arial 12 bold", command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        #dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                  font="Arial 12 bold", command=partial(self.close_history,partner))
        self.dismiss_button.grid(row=0, column=1)
                                  

        
    def close_history(self, partner):
        # put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self,calc_history):
        Export(self, calc_history)


class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)
        
        background = "#a9ef99"

        #disable export button
        partner.export_button.config(state=DISABLED)

        #sets up a child window (export box)
        self.export_box=Toplevel()

        self.export_box.protocol('WM_DELETE_WINDOW',partial(self.close_export, partner))

        #set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        #set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        #export instructions (label row1)
        self.export_text = Label(self.export_frame, text="Enter a filename "
                                 "in the box below "
                                 "and press the Save "
                                 "button to save your "
                                 "calculation history "
                                 "to a text file", wrap=250,
                                  justify=LEFT, width=40,
                                  bg=background)
        self.export_text.grid(row=1)

        #warning text (row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you enter below "
                                 "already exists, "
                                 "its contents will "
                                 "be replaced with "
                                 "your calculation "
                                 "history", wrap=225,
                                  justify=LEFT, fg="maroon",
                                  bg="#ffafaf", padx=10, pady=10, font="arial 10 italic")
        self.export_text.grid(row=2, pady=10)

        #filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        #error message labels (initiall blank, row4)
        self.save_error_label = Label(self.export_frame, text="",fg="maroon",bg=background)
        self.save_error_label.grid(row=4)

        #save/canel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        #save and cancel buttons (row 0 of save cancel)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  font="Arial 12 bold",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)
        
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                  font="Arial 12 bold", command=partial(self.close_export,partner))
        self.cancel_button.grid(row=0, column=1)
                                  
    def save_history(self,partner,calc_history):

        #regular expression to check if filename is valid
        valid_char  = "[A-Za-z0-9_]"
        has_error="no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no []'s allowed)".format(letter))
            has_error = "yes"
            break
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            #display error message
            self.save_error_label.config(text="Invalid filname - {}".format(problem))
            #change entry box to pink
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            #if there are no errors generate a text file and close dialogue
            #add .txt suffix
            filename = filename + ".txt"

            #create file to hold data
            f = open(filename, "w+")

            #add new line at end of each item
            for item in calc_history:
                f.write(item + "\n")

            #close file
            f.close()

            #close dialogue
            self.close_export(partner)
        
    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

class Help:
    def __init__(self, partner):
        background = "orange"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #sets up a child window (help box)
        self.help_box=Toplevel()

        self.help_box.protocol('WM_DELETE_WINDOW',partial(self.close_help, partner))

        #set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        #set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        #help text (label row1)
        self.help_text = Label(self.help_frame, text="",wrap=250,
                                  justify=LEFT, bg=background)
        self.help_text.grid(row=1)
         
        #dismiss button frame (row 3)
        self.dismiss_frame = Frame(self.help_frame)
        self.dismiss_frame.grid(row=3, pady=10)

        #dismiss button
        self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                  font="Arial 12 bold", command=partial(self.close_help,partner))
        self.dismiss_button.grid(row=3, column=0)
                                  
        
    def close_help(self, partner):
        # put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()
        

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()


