#from modules.card_system import *

#from modules.money_system import *
from tkinter import *
from functools import partial

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
        self.main_buttons(None)
        self.buttonframe.pack(fill="x", padx=30, pady=30, side=BOTTOM) # x is for x-axis
        self.mynum = IntVar()

        self.root.mainloop()


    def show_buttons(self, btns):

        if btns:
            self.reset_btns(btns)

        quarter_btn = Button(self.buttonframe, text="25% pot", font=('Arial', 18), fg='#7ca5f2')
        half_btn = Button(self.buttonframe, text="50% pot", font=('Arial', 18), fg='#5289f0')
        three_quarters_btn = Button(self.buttonframe, text="75% pot", font=('Arial', 18), fg='#135fed')
        full_btn = Button(self.buttonframe, text="100% pot", font=('Arial', 18), fg='#043ca7')
        go_back_btn = Button(self.buttonframe, text="Go back", font=('Arial', 18))
        custom_btn = Button(self.buttonframe, text="Custom", font=('Arial', 18), fg='#8132a8')
        shows = [quarter_btn, half_btn, three_quarters_btn, full_btn, custom_btn, go_back_btn] # based on grid placement
        custom_btn.configure(command=partial(self.enter_custom, shows))

        quarter_btn.grid(row=0, column=0, sticky=W+E)
        half_btn.grid(row=0, column=1, sticky=W+E)
        three_quarters_btn.grid(row=0, column=2, sticky=W+E)
        full_btn.grid(row=0, column=3, sticky=W+E)
        custom_btn.grid(row=0, column=4, sticky=W+E)
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

        if self.color_mode:
            self.light_mode_on()
        else:
            self.dark_mode_on()


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
            self.mynum = 0
            print(num)
            self.reset_btns(btns)
            self.main_buttons(None)

    def reset_btns(self, btns):
        for i in btns:
            i.grid_forget()


Poker_Gui()
