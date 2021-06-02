#!/usr/bin/env python

import yaml
from map_cell import MapCell


def parse_yaml():
    """
    Parse yaml to python dict
    """
    file_path = "./input.yaml"
    with open(file_path) as file:
        yaml_parsed = yaml.safe_load(file)
    return yaml_parsed


def init_map(yaml_content):
    """
    Init the game map according to parsed yaml
    """
    map_length = yaml_content["length"]

    dragons_only = yaml_content["dragons"]

    princess_only = yaml_content["princess"]

    playground = []

    for i in range(map_length):
        playground.append(None)

    for key, val in dragons_only.items():
        playground[key] = MapCell("d", val)

    for key, val in princess_only.items():
        playground[key] = MapCell("p", val)

    return playground


def calculate_dragons(princess_index, playground):
    """
    get rid of all non relevant dragons so we can marry the N-th princess as per block
    """
    max_of_dragons = playground[princess_index].amount - 1
    dragons_list_till_princess = []
    for cell in playground[:princess_index]:
        if cell and cell.cell_type == "d":
            dragons_list_till_princess.append(cell)
    dragons_gold = []
    for dragon in dragons_list_till_princess:
        dragons_gold.append(dragon.amount)
    max_n_dragons_gold = sorted(dragons_gold, reverse=True)[:max_of_dragons]

    dragons_indexes_to_kill = []
    for gold in max_n_dragons_gold:
        for i, cell in enumerate(playground[:princess_index]):
            if cell and cell.cell_type == "d" and cell.amount == gold and i not in dragons_indexes_to_kill:
                dragons_indexes_to_kill.append(i)
                break

    for i, cell in enumerate(playground[:princess_index]):
        if i not in dragons_indexes_to_kill:
            playground[i] = None


def check_optimal_path(playground):
    """
    Check if we can marry the N-th princess
    """
    tmp_list = []
    for i, cell in enumerate(playground):
        if cell and cell.cell_type == "p":
            tmp_list.append(i)
    last_not_N_princess_index = tmp_list[-2]

    for i, cell in enumerate(playground[:last_not_N_princess_index + 1]):
        if cell and cell.cell_type == "p":
            calculate_dragons(i, playground)


def create_summary(playground):
    """
    Insight conclusions and print summary
    """
    total_dragons_to_kill = 0
    for cell in playground[:-1]:
        if cell and cell.cell_type == "d":
            total_dragons_to_kill += 1
    if total_dragons_to_kill < playground[-1].amount:
        print(-1)
    else:
        total_gold_earned = 0
        dragons_index = []
        for i, cell in enumerate(playground[:-1]):
            if cell and cell.cell_type == "d":
                total_gold_earned += cell.amount
                dragons_index.append(str(i + 1))

        print(total_gold_earned)
        print(total_dragons_to_kill)
        print(" ".join(dragons_index))


def main():
    yaml_parsed = parse_yaml()
    playground = init_map(yaml_parsed)
    check_optimal_path(playground)
    create_summary(playground)


if __name__ == "__main__":
    main()