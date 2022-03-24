from tkinter import *

class Converter:
    def __init__(self):

        #formatting variables
        background_color = "light blue"

        #converter frame
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        #temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                         text="Temperature Converter",
                                 font="arial 16 bold", bg=background,
                                         padx = 10, pady=10)
        self.temp_heading_label.grid(row=0)

        #user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                             "convertered and then push"
                                             "one of the buttons below...",
                                             font="arial 16 italic",wrap=250,
                                             justify=LEFT,bg=background,
                                         padx = 10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #temperature entry box (row 2)

        #conversion buttons frame (row 3)

        #answer label (row 4)

        #history / help button frame (row 5)
