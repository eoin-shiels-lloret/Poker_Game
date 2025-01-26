import modules.card_system as cards
import modules.money_system as money
from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import random

class Poker_Gui(object):

    def __init__(self):


        self.root = Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Poker Game")
        self.display_height=self.root.winfo_screenheight()
        self.display_width=self.root.winfo_screenwidth()
        self.label = Label(self.root, text="Pot Value", font=('Arial', 20), height=2, width=12)
        self.label.pack(padx=10, pady=15)
        self.root.bind("<Escape>", self.end_fullscreen)

        # create the buttonframe, might make this a function like main_buttons in the future
        self.buttonframe = Frame(self.root, highlightbackground="black", highlightthickness=4, width=1000, height=800)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)
        self.buttonframe.columnconfigure(4, weight=1)

        # start on lightmode, set color_mode to true
        self.light_mode_on()
        self.color_mode = True # True is for light mode
        # fill in the buttonframe, pass None in as there are no buttons to remove/reset
        self.main_buttons(None)
        self.buttonframe.pack(fill="x", padx=30, pady=30, side=BOTTOM) # x is for x-axis
        self.initialise_deck()
        self.mynum = IntVar()

        self.root.mainloop()


    def show_buttons(self, btns):

        if btns:
            self.reset_btns(btns)

        quarter_btn = Button(self.buttonframe, text="25% pot", font=('Arial', 18), fg='#7ca5f2')
        half_btn = Button(self.buttonframe, text="50% pot", font=('Arial', 18), fg='#5289f0')
        full_btn = Button(self.buttonframe, text="100% pot", font=('Arial', 18), fg='#043ca7')
        go_back_btn = Button(self.buttonframe, text="Go back", font=('Arial', 18))
        custom_btn = Button(self.buttonframe, text="Custom", font=('Arial', 18), fg='#8132a8')

        shows = [quarter_btn, half_btn, full_btn, custom_btn, go_back_btn] # based on grid placement
        custom_btn.configure(command=partial(self.enter_custom, shows))

        quarter_btn.grid(row=0, column=0, sticky=W+E)
        half_btn.grid(row=0, column=1, sticky=W+E)
        full_btn.grid(row=0, column=2, sticky=W+E)
        custom_btn.grid(row=0, column=3, sticky=W+E)
        go_back_btn.grid(row=0, column=5, sticky=W+E)
        go_back_btn.configure(command=partial(self.main_buttons, shows))

    def main_buttons(self, btns):

        if btns:
            self.reset_btns(btns)

        fold_btn = Button(self.buttonframe, text="Fold", font=('Arial', 18), fg="red")
        check_btn = Button(self.buttonframe, text="Check", font=('Arial', 18), fg="blue")
        raise_btn = Button(self.buttonframe, text="Raise", font=('Arial', 18), fg="orange")
        call_btn = Button(self.buttonframe, text="Call", font=('Arial', 18), fg="magenta")

        mains = [fold_btn, check_btn, call_btn, raise_btn]
        raise_btn.configure(command=partial(self.show_buttons, mains))

        fold_btn.grid(row=0, column=0, sticky=W+E)  # w+e is west and east
        check_btn.grid(row=0, column=1, sticky=W+E)
        raise_btn.grid(row=0, column=3, sticky=W+E)
        call_btn.grid(row=0, column=2, sticky=W+E)

    def dark_mode_on(self):

        self.root.configure(background="#023020", highlightbackground="#F0FCCE", highlightthickness=8)
        self.label.configure(background="#023020", fg="#F0FCCE")
        light_mode_btn = Button(self.buttonframe, text="Light Mode", font=('Arial', 16), command=self.light_mode_on)
        light_mode_btn.grid(row=0, column=4, sticky=W+E)
        self.color_mode = False

    def light_mode_on(self):

        self.root.configure(background="green", highlightbackground="brown", highlightthickness=8)
        self.label.configure(background="green", fg="black")
        dark_mode_btn = Button(self.buttonframe, text="Dark Mode", font=('Arial', 16), command=self.dark_mode_on)
        dark_mode_btn.grid(row=0, column=4, sticky=W+E)
        self.color_mode = True

    def enter_custom(self, btns):

        go_back_btn = btns.pop(-1)
        self.reset_btns(btns)
        bet_input = Entry(self.buttonframe, width=20, textvariable=self.mynum)
        bet_input.grid(row=0, column=1, sticky=W+E)
        submit_btn = Button(self.buttonframe, text="Submit: ")
        submit_btn.grid(row=0, column=2, sticky=W+E)
        customs = [bet_input, submit_btn, go_back_btn]
        submit_btn.configure(command=partial(self.remove_and_run, customs))
        go_back_btn.configure(command=partial(self.main_buttons, customs))


    def remove_and_run(self, btns):

        if btns[1]['text'] == 'Submit: ':

            num = self.mynum.get()
            self.mynum = IntVar()
            print(num)
            self.reset_btns(btns)
            self.main_buttons(None)

    def reset_btns(self, btns):
        for i in btns:
            i.grid_forget()

    def end_fullscreen(self, event=None):
        self.root.attributes("-fullscreen", False)
        self.root.geometry('1000x800')
        return 'break'

    def initialise_deck(self):

        # weird bug means i have to make these global (to stop garbage collection)
        global img1, img2, img3
        self.deck = cards.make_deck()
        random.shuffle(self.deck)
        img1 = PhotoImage(file=self.deck[0].image)
        img2 = PhotoImage(file=self.deck[3].image)
        img3 = PhotoImage(file=self.deck[10].image)

        river_card1 = Label(self.root, height=183, width=126, image=img1)
        river_card2 = Label(self.root, height=183, width=126, image=img2)
        river_card3 = Label(self.root, height=183, width=126, image=img3)

        print(self.root.attributes("-fullscreen"))
        c1_width = (self.display_width / 5) if not self.root.attributes("-fullscreen") else 30
        print(c1_width)

        river_card1.pack(side=LEFT, padx=(c1_width, 0))
        river_card2.pack(side=LEFT)
        river_card3.pack(side=LEFT)

Poker_Gui()
