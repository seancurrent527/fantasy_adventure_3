'''
Implements setup for human players in FA3.
'''
import base_setup as bs
import actions_list as act

CLASSES = {'Warrior': [110, 110, 100, 80], 'Rogue': [90, 100, 90, 120], 'Mage': [80, 130, 90, 100], 'Cleric': [130, 90, 110, 70]}
ACTIONS = [act.Firebolt, act.Strike, act.Quickshot, act.Relief]
ALL_ACTIONS = [act.Firebolt, act.Icicle, act.Thunder, act.Absorb,
               act.Strike, act.Parry, act.Block, act.Slash,
               act.Quickshot, act.Flash, act.Toxic, act.Stealth,
               act.Relief, act.Heal, act.Smite, act.Prayer]

def new_character(classes, base_actions):
    name = input('Enter a name for the character: ')
    player = None
    while player is None:
        print('Choose a class:')
        for clas in classes:
            print(clas + '-- HP: {}  ATK: {}  DEF: {}  SPD: {}'.format(*classes[clas]))
        print()
        choice = input()
        print()
        if choice not in classes:
            print('You cannot choose that class.')
            continue    
        player = bs.Character(name, *classes[choice])
    for i in range(2):
        player.level_up(base_actions)
    return player













