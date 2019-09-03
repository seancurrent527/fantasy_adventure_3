'''
Actions and effects list for FA3.
'''

import base_setup as bs

# Common effect functions:
def dot(p, d): 
    p.hp -= d
def stun(p, d): 
    p.delay = d
def shock(p, d): 
    p.df *= d; p.atk *= d
def regen(p, d): 
    p.hp += d
def buff(p, d): 
    p.df *= d; p.atk *= d
def quicken(p, d): 
    p.spd *= d
def slow(p, d): 
    p.spd *= d
def harden(p, d):
    p.df *= d
def clear(p, d):
    p.effects = []
def hidden(p, d):
    p.spd *= 0
    p.atk *= d
def weaken(p, d):
    p.df *= d

# Common Effects:
burned = bs.Effect('burned', dot, 4, 2)
poisoned = bs.Effect('poisoned', dot, 2, 5)
stunned = bs.Effect('stunned', stun, True, 1)
shocked = bs.Effect('shocked', shock, 0.92, 3, instant=True)
slowed = bs.Effect('slowed', slow, 0.75, 2)
regenerated = bs.Effect('regenerated', regen, 4, 3)
buffed = bs.Effect('buffed', buff, 1.12, 2, instant=True)
quickened = bs.Effect('quickened', quicken, 1.5, 1)


# Player Abilities:
Firebolt = bs.Action('Firebolt', 90, (3,4), 0, burned, None,
    message= lambda p1, p2: p1.name + ' casts firebolt for 3-4 damage! ' + p2.name + ' is burned!')
Icicle = bs.Action('Icicle', 80, (5,6), 0, slowed, None, 
    message= lambda p1, p2: p1.name + ' casts icicle for 5-6 damage! ' + p2.name + ' is slowed!')
Thunder = bs.Action('Thunder', 70, (15,20), 0, shocked, None, 
    message= lambda p1, p2: p1.name + ' casts thunder for 15-20 damage! ' + p2.name + ' is shocked!')
Absorb = bs.Action('Absorb', 70, 2, 2, effect1= bs.Effect('drained', dot, 2, 6), effect2= bs.Effect('regenerated', regen, 2, 6),
    message= lambda p1, p2: p1.name + ' prepares to absorb hp from ' + p2.name + '!')
Strike = bs.Action('Strike', 100, (7,8), 0, message= lambda p1, p2: p1.name + ' strikes ' + p2.name + ' for 7-8 damage!')
Parry = bs.Action('Parry', 95, 0, 0, effect2= bs.Effect('parrying', buff, 1.5, 0, instant=True), 
    message= lambda p1, p2: p1.name + ' prepares to parry! They will take less damage and deal more for 1 turn!')
Block = bs.Action('Block', 90, 0, 0, effect2= bs.Effect('blocking', harden, 10, 0, instant=True),
    message= lambda p1, p2: p1.name + ' prepares to block! Their defense is greatly increased for 1 turn!')
Slash = bs.Action('Slash', 85, (4,5), 0, effect1= bs.Effect('bled', dot, 8, 1),
    message= lambda p1, p2: p1.name + ' slashes '+ p2.name + ' for 4-5 damage! ' + p2.name + ' is bleeding!')
Quickshot = bs.Action('Quickshot', 100, 5, 0, effect2= quickened,
    message= lambda p1, p2: p1.name + ' fires a quickshot at ' + p2.name + ' for 4-5 damage! ' + p1.name + '\'s speed is increased!')
Flash = bs.Action('Flash', 50, 0, 0, bs.Effect('disoriented', stun, True, 1, instant=True),
    message= lambda p1, p2: p1.name + ' releases a flash of light, disorienting ' + p2.name + '! They will not be able to make an action for two turns.')
Toxic = bs.Action('Toxic', 100, 2, 0, effect1= poisoned, 
    message= lambda p1, p2: p1.name + ' fires a toxic dart at ' + p2.name + ' for 2 damage! ' + p2.name + ' is poisoned!')
Stealth = bs.Action('Stealth', 80, 0, 0, effect2= bs.Effect('hidden', hidden, 5, 0, instant=True),
    message= lambda p1, p2: p1.name + ' prepares a hidden attack!')
Relief = bs.Action('Relief', 90, 0, 0, effect2= bs.Effect('relieved of all effects', clear, None, 0, instant=True),
    message= lambda p1, p2: p1.name + ' clears themselves of all effects!')
Heal = bs.Action('Heal', 90, 0, (10,12), message= lambda p1, p2: p1.name + 'casts heal for 10-12 hp!')
Smite = bs.Action('Smite', 85, (6,7), 0, effect1= bs.Effect('weakened', weaken, 0.75, 3, instant=True),
    message= lambda p1, p2: p1.name + ' smites ' + p2.name + ' for 6-7 damage! ' + p2.name + '\'s defenses are lowered!')
Prayer = bs.Action('Prayer', 100, 0, 0, effect2 = bs.Effect('strengthened', harden, 1.5, 3, instant=True),
    message= lambda p1, p2: p1.name + ' prays for strength! Their defenses are greatly increased!')