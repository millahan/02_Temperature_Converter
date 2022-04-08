from tkinter import *
from functools import partial
#import random

class Converter:
    def __init__(self,parent):

        # formatting variables...
        background_color = "light blue"

        # converter main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature conversion heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,text="Temperature Converter",
                                          font = ("Arial","16","bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
 
        # export button (row 1)
        self.export_button = Button(self.converter_frame, text="Export",
                                  font=("Arial""14"),
                                  padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):

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

        #save/canel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        #save and cancel buttons
        self.save_button = Button(self.save_cancel_frame, text="Save",font="Arial 12 bold")
        self.save_button.grid(row=0, column=0)
        
        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                  font="Arial 12 bold", command=partial(self.close_export,partner))
        self.cancel_button.grid(row=0, column=1)
                                  

        
    def close_export(self, partner):
        # put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()
        

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter(root)
    root.mainloop()


