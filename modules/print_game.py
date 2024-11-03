#!/usr/bin/env python3

import card_system
import money_system

from tkinter import *
from tkinter import ttk

class Poker_Gui(object):

    def __init__(self):

        self.root = Tk()
        self.root.geometry('1000x800')
        self.root.title("Poker Game")
        self.root.configure(background="green", highlightbackground="black", highlightthickness=8)

        self.label = Label(self.root, text="Make the best hand to win!", font=('Arial', 20))
        self.label.pack(padx=10, pady=10)
        self.label.configure(background="green")

        self.buttonframe = Frame(self.root, highlightbackground="black", highlightthickness=4, width=1000, height=800)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        self.fold_button = Button(self.buttonframe, text="Fold", font=('Arial', 18), fg="red")
        self.check_button = Button(self.buttonframe, text="Check", font=('Arial', 18), fg="blue")
        self.raise_button = Button(self.buttonframe, text="Raise", font=('Arial', 18), fg="orange", command=self.show_button)
        self.call_button = Button(self.buttonframe, text="Call", font=('Arial', 18), fg="magenta")

        self.fold_button.grid(row=0, column=0, sticky=W+E)  # w+e is west and east
        self.check_button.grid(row=0, column=1, sticky=W+E)
        self.raise_button.grid(row=0, column=3, sticky=W+E)
        self.call_button.grid(row=0, column=2, sticky=W+E)

        self.buttonframe.pack(fill="x", padx=30, pady=30, side=BOTTOM) # x is for x-axis


        self.root.mainloop()

    def show_button(self):

        quarter_button = Button(self.buttonframe, text="25% pot", font=('Arial', 18))
        half_button = Button(self.buttonframe, text="50% pot", font=('Arial', 18))
        three_quarters_button = Button(self.buttonframe, text="75% pot", font=('Arial', 18))
        full_button = Button(self.buttonframe, text="100% pot", font=('Arial', 18))

        quarter_button.grid(row=0, column=0, sticky=W+E)
        half_button.grid(row=0, column=1, sticky=W+E)
        three_quarters_button.grid(row=0, column=2, sticky=W+E)
        full_button.grid(row=0, column=3, sticky=W+E)

Poker_Gui()
