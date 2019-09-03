'''
Main thread for FA3.
'''

import battle_setup as btl
import character_setup as chars
import enemies_list as enemies

def main():
    player = chars.new_character(chars.CLASSES ,chars.ACTIONS)
    playing = True
    while playing:
        print('\nYou are fighting The Goblin!\n')
        winner = btl.battle(player, enemies.Goblin)
        if winner is player:
            print('You have defeated The Goblin! Level up and play again? (y|n)')
            playing = input().lower()[0] == 'y'
            playing and player.gain_exp(200, chars.ALL_ACTIONS)
        else:
            print('You have failed your quest. play again? (y|n)')
            playing = input().lower()[0] == 'y'
    print('Goodbye!')

if __name__ == '__main__':
    main()