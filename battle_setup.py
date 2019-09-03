'''
Battle setup for FA3 between two characters.
'''

import base_setup as bs
import random

def print_info(*players):
    print()
    for p in players:
        printer = p.name.ljust(max(map(lambda p: len(p.name), players))) + ' |'
        ratio = p.hp/p.base_hp
        blocks = int(ratio * 20)
        printer += '\u2588' * blocks + ' ' * (20 - blocks) + '|'
        printer += ' ' + str(round(p.hp, 2)) + ' / ' + str(p.base_hp)
        print(printer)
    print()

def play_order(p1, p2):
    options = ([p1, p2], [p2, p1])
    if p1.spd == p2.spd:
        return random.choice(options)
    else:
        return options[0] if p1.spd > p2.spd else options[1]

def winner(p1, p2):
    if p1.hp > p2.hp:
        print(p1.name + ' is victorious!')
        return p1
    else:
        print(p2.name + ' has defeated ' + p1.name + '!')
        return p2

def battle(p1, p2):
    p1.reset(); p2.reset()
    p1.max_hp(); p2.max_hp()
    chooser = lambda p: p.choose_action() if not p.computer else p.computer_action() 
    while p1.is_alive() and p2.is_alive():
        first, second = play_order(p1, p2)    
        print('The play order is:', first, second, '', sep = '\n')
        print_info(p1, p2)
        act = chooser(first)
        first.apply_action(second, act)
        first.apply_effects()
        print_info(p1, p2)
        if not (second.is_alive() and p2.is_alive()):
            break
        act = chooser(second)
        second.apply_action(first, act)
        second.apply_effects()
        print_info(p1, p2)
    return winner(first, second)
    



























