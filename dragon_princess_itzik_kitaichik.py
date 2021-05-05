#!/usr/bin/env python3.6

import yaml

__author__= "Itzik Kitaichik"
__version__ = "1.0.0"
__email__ = "rayrayids@gmail.com"
__status__ = "Complete"


def main_game(file_name):
    game_map = file_name['size']
    map_end = game_map - 1
    actual_map = file_name['levels']
    dead_dragons = []

    # len([npc['d'] for npc in actual_map if 'd' in npc])  =  number of total dragons in game
    # if last princess has beauty > max dragons, return -1

    try:
        if actual_map[-1]['p'] > len([npc['d'] for npc in actual_map if 'd' in npc]):
            return -1
    except KeyError:
        return -1

    for pos, index in enumerate(actual_map, start=1):
        if [*index.keys()] == ['d']:
            dead_dragons.append((pos, index['d']))
        elif [*index.keys()] == ['p'] and pos != map_end:
            # Loop to find best dragon if potential married to wrong princess is met
            while len(dead_dragons) >= index['p']:
                # remove lowest value dragon from list
                lowest_dragon = min(dead_dragons, key=lambda low_coin: low_coin[1])
                dead_dragons.remove(lowest_dragon)
        elif pos == map_end:
            if len(dead_dragons) < int(index['p']):
                return -1

    total_gold = str(sum([pos[1] for pos in dead_dragons]))

    dragons_positions = str(list(pos[0]+1 for pos in dead_dragons))

    game_result = [total_gold, len(dead_dragons), dragons_positions[1:-1]]

    # Return a list for future processing if needed, could also return concatenated strings

    return game_result


if __name__ == "__main__":
    # Testing without yaml
    # Could us below code for unit testing, either static or code generated yaml

    # game_layout = {
    #     'size': 7,
    #     'levels': [
    #         {
    #             'd': 10,
    #         },
    #         {
    #             'd': 23
    #         },
    #         {
    #             'd': 22
    #         },
    #         {
    #             'p': 2
    #         },
    #         {
    #             'd': 6
    #         },
    #         {
    #             'p': 2
    #         }
    #     ]
    # }

    with open("test.yaml", 'r') as options:
        game_layout = yaml.safe_load(options)

    output = main_game(game_layout)
    if output == -1:
        print(output)
    else:
        for res in output:
            print(res)
