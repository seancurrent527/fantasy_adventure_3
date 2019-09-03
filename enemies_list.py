'''
The enemy list for FA3. Prepares computer players.
'''

import base_setup as bs
import actions_list as act

Goblin = bs.Character('The Goblin', 70, 100, 100, 100, True, actions = [act.Strike, act.Toxic, act.Block], probabilities = [0.7, 0.2, 0.1])