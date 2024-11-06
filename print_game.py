from modules.card_system import *
from modules.money_system import *
from tkinter import *

class Poker_Gui(object):

    def __init__(self):

        self.root = Tk()
        self.root.geometry('1000x800')
        self.root.title("Poker Game")

        self.label = Label(self.root, text="Pot Value", font=('Arial', 20), height=2, width=12)
        self.label.pack(padx=10, pady=15)

        self.buttonframe = Frame(self.root, highlightbackground="black", highlightthickness=4, width=1000, height=800)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)
        self.buttonframe.columnconfigure(4, weight=1)

        self.light_mode_on()
        self.color_mode = True # True is for light mode
        self.main_buttons()
        self.buttonframe.pack(fill="x", padx=30, pady=30, side=BOTTOM) # x is for x-axis

        self.root.mainloop()

    def show_buttons(self):

        quarter_button = Button(self.buttonframe, text="25% pot", font=('Arial', 18), fg='#7ca5f2')
        half_button = Button(self.buttonframe, text="50% pot", font=('Arial', 18), fg='#5289f0')
        three_quarters_button = Button(self.buttonframe, text="75% pot", font=('Arial', 18), fg='#135fed')
        full_button = Button(self.buttonframe, text="100% pot", font=('Arial', 18), fg='#043ca7')
        go_back_button = Button(self.buttonframe, text="Go back", font=('Arial', 18), command=self.main_buttons)

        quarter_button.grid(row=0, column=0, sticky=W+E)
        half_button.grid(row=0, column=1, sticky=W+E)
        three_quarters_button.grid(row=0, column=2, sticky=W+E)
        full_button.grid(row=0, column=3, sticky=W+E)
        go_back_button.grid(row=0, column=4, sticky=W+E)

    def main_buttons(self):

        fold_button = Button(self.buttonframe, text="Fold", font=('Arial', 18), fg="red")
        check_button = Button(self.buttonframe, text="Check", font=('Arial', 18), fg="blue")
        raise_button = Button(self.buttonframe, text="Raise", font=('Arial', 18), fg="orange", command=self.show_buttons)
        call_button = Button(self.buttonframe, text="Call", font=('Arial', 18), fg="magenta")
        if self.color_mode:
            self.light_mode_on()
        else:
            self.dark_mode_on()


        fold_button.grid(row=0, column=0, sticky=W+E)  # w+e is west and east
        check_button.grid(row=0, column=1, sticky=W+E)
        raise_button.grid(row=0, column=3, sticky=W+E)
        call_button.grid(row=0, column=2, sticky=W+E)

    def dark_mode_on(self):

        self.root.configure(background="#023020", highlightbackground="#F0FCCE", highlightthickness=8)
        self.label.configure(background="#023020", fg="#F0FCCE")
        light_mode_button = Button(self.buttonframe, text="Light Mode", font=('Arial', 16), command=self.light_mode_on)
        light_mode_button.grid(row=0, column=4, sticky=W+E)

    def light_mode_on(self):

        self.root.configure(background="green", highlightbackground="brown", highlightthickness=8)
        self.label.configure(background="green", fg="black")
        dark_mode_button = Button(self.buttonframe, text="Dark Mode", font=('Arial', 16), command=self.dark_mode_on)
        dark_mode_button.grid(row=0, column=4, sticky=W+E)

Poker_Gui()
