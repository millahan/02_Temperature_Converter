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
                                 font="arial 16 bold", bg=background_color,
                                         padx = 10, pady=10)
        self.temp_heading_label.grid(row=0)

        #user instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be"
                                             "convertered and then push"
                                             "one of the buttons below...",
                                             font="arial 16 italic",wrap=250,
                                             justify=LEFT,bg=background_color,
                                         padx = 10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width =20,
                                      font="arial 14 bold")
        self.to_convert_entry.grid(row=2)
        

        #conversion buttons frame (row 3)
        self.conversion_buttons_frame =Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="arial 10 bold",
                                  bg ="khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0,column=0)
        
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="arial 10 bold",
                                  bg ="orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0,column=1)

        #answer label (row 4)

        #history / help button frame (row 5)

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
    
