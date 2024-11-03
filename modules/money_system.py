#!/usr/bin/env python3

class Chip(object):

    def __init__(self, amount, value):
        self.amount = amount            # Would this be better with a dictionary????
        self.value = value

class Chip_Stack(object):

    def __init__(self, is_pot=False):
        self.stack = {}
        self.is_pot = is_pot

    def add_chips(self, chips):

        for i in chips:
            self.stack[i.value] = i.amount # took me forever to realise amount had to be second cause you cant have multiple keys of the same value

    def transfer(self, other, cost): # this is for transferring between the pot and player_stack

        print(f"You bet {cost} Euros")
        self.change(cost, "-")
        other.change(cost, "+")

    def change(self, cost, operation):

        for value, amount in self.stack.items():
            diff = cost // value
            if operation == "+":
                self.stack[value] = amount + diff
            elif operation == "-":
                self.stack[value] = amount - diff
            cost -= diff * value

    def total(self):

        total_chips_value = 0
        for i in self.stack:
            total_chips_value += (i * self.stack[i]) # multiplies chip value by chip amount

        if self.is_pot:
            return f"Pot size is {total_chips_value} Euros"
        else:
            return f"You have {total_chips_value} Euros left"

def make_stacks():

    player_stack = Chip_Stack()
    player_stack_default = (Chip(2, 100), Chip(3, 50), Chip(5, 10), Chip(10, 5), Chip(50, 1))
    player_stack.add_chips(player_stack_default)

    pot = Chip_Stack(True)
    pot_default = (Chip(0, 100), Chip(0, 50), Chip(0, 10), Chip(0, 5), Chip(0, 1))
    pot.add_chips(pot_default)

    return player_stack, pot

#stacks = make_stacks()
#print(stacks[0].stack, stacks[0].is_pot, stacks[1].stack, stacks[1].is_pot)
#player = stacks[0]
#pot = stacks[1]

#print(pot.total(), player.total())
#player.transfer(pot, 259)
#print(pot.total(), player.total())


