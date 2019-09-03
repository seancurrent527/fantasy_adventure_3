'''
Class Setup for FA3. This implements characters, effects, and actions.
'''

import random

class Character:
    def __init__(self, name, hp, atk, df, spd, computer = False, actions = [], probabilities = None):
        self.name = name
        self.base_hp = hp
        self.base_atk = atk
        self.base_df = df
        self.base_spd = spd
        self.hp = self.base_hp
        self.atk = self.base_atk
        self.df = self.base_df
        self.spd = self.base_spd
        self.delay = False
        self.computer = computer
        self.probabilities = probabilities
        self.level = 1
        self.exp = 0
        self.actions = actions
        self.effects = []
        self.effect_durations = {}

    def __repr__(self):
        return self.name

    def choose_action(self):
        if self.delay:
            print(self.name + ' cannot make an action!\n')
            return Action('', 100, 0, 0)
        names = [act.name for act in self.actions]
        while True:
            print('Choose an action:', *names, sep = '\n')
            print()
            choice = input()
            print()
            if choice not in names:
                print('That is not one of your actions.\n')
            else:
                return self.actions[names.index(choice)]

    def computer_action(self):
        assert len(self.probabilities) == len(self.actions)
        choice = random.random()
        total = 0
        for i in range(len(self.probabilities)):
            total += self.probabilities[i]
            if choice < total:
                return self.actions[i]

    def apply_action(self, other, action):
        print()
        if random.random() * 100 < action.accuracy:
            action.applyto(other, self)
        else:
            print(action.name +' misses!')

    def apply_effects(self):
        self.reset()
        for eff in self.effects:
            if self.effect_durations[eff] > 0:
                eff.applyto(self)
                self.effect_durations[eff] -= 1
        self.hp = min(self.hp, self.base_hp)

    def reset(self):
        self.hp = min(self.hp, self.base_hp)
        self.atk = self.base_atk
        self.df = self.base_df
        self.spd = self.base_spd
        self.delay = False

    def is_alive(self):
        return self.hp > 0

    def learn(self, action):
        self.actions.append(action)
        print(self.name + ' learned ' + action.name + '!')

    def gain_exp(self, exp, actions):
        self.exp += exp
        print(self.name + ' gained ' + str(exp) + ' xp!')
        while self.exp >= (self.level) * (self.level + 1) / 2 * 100:
            self.level += 1
            print(self.name + ' leveled up! ' + self.name + ' is level ' + str(self.level) + '.')
            self.level_up(actions)

    def level_up(self, actions):
        actions = [a for a in actions if a not in self.actions]
        names = [a.name for a in actions]
        stats = {'Speed': 0, 'Defense': 0, 'Attack': 0, 'Health': 0}
        while True:
            print('Choose a stat to increase:', *stats.keys(), sep = '\n')
            print()
            choice = input()
            print()
            if choice not in stats:
                print('You cannot improve that stat.\n')
            else:
                stats[choice] = 10
                self.base_spd += stats['Speed'] 
                self.base_df += stats['Defense']
                self.base_atk += stats['Attack']
                self.base_hp += stats['Health']
                break
        while True:
            print('Choose an action to learn:', *names, sep = '\n')
            print()
            choice = input()
            print()
            if choice not in names:
                print('You cannot learn that action.\n')
            else:
                self.learn(actions[names.index(choice)]) 
                break   

    def max_hp(self):
        self.hp = self.base_hp

class Effect:

    def __init__(self, name, function, degree, turns, instant = False):
        self.name = name
        self.degree = degree
        self.function = lambda p: function(p, degree)
        self.turns = turns
        self.instant = instant

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name + str(self.degree))

    def __eq__(self, other):
        return self.name == other.name and self.degree == other.degree

    def __gt__(self, other):
        return self.turns > other.turns

    def __lt__(self, other):
        return self.turns < other.turns

    def message(self, other):
        return other.name + ' is ' + self.name + '!'

    def applyto(self, other):
        print(self.message(other))
        self.function(other)

class Action:
    def __init__(self, name, accuracy, dmg, heal, effect1 = None, effect2 = None, message = lambda p1, p2: ''):
        self.name = name
        self.accuracy = accuracy
        self.dmg = dmg
        self.heal = heal
        self.effect1 = effect1
        self.effect2 = effect2
        self.message = message

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def applyto(self, p1, p2):
        evalu = lambda val: random.randint(*val) if type(val) is tuple else val
        print(self.message(p2, p1))
        p1.hp -= (p2.atk/p1.df)*evalu(self.dmg); p2.hp += (p2.df/100)*evalu(self.heal)
        if self.effect1 is not None:
            self.effect1 not in p1.effects and p1.effects.append(self.effect1) 
            p1.effect_durations[self.effect1] = self.effect1.turns
            self.effect1.instant and self.effect1.applyto(p1)
        if self.effect2 is not None:
            self.effect2 not in p2.effects and p2.effects.append(self.effect2)
            p2.effect_durations[self.effect2] = self.effect2.turns
            self.effect2.instant and self.effect2.applyto(p2)