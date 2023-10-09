#!/usr/bin/python
import argparse
import sys
import subprocess

# Make sure yaml package is installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
import yaml

def read_yaml_file(yaml_file_path):
    with open('parameters.yaml', 'r') as file:
        return yaml.safe_load(file)

def calculate_max_gold(data):
    n = data['n']-1
    items = data['items']
    cells = [(item['type'], item['value']) for item in items]

    max_gold = 0
    dragons_to_kill = []

    def backtrack(current_cell, current_gold, dragons_killed):
        nonlocal max_gold, dragons_to_kill

        if current_cell == n:
            if len(dragons_killed) < cells[current_cell - 1][1]:
                return -1
            elif current_gold > max_gold:
                max_gold = current_gold
                dragons_to_kill = dragons_killed.copy()
            return

        next_cell = current_cell + 1

        backtrack(next_cell, current_gold, dragons_killed)  # Option 1: Skip the current cell

        if cells[current_cell - 1][0] == 'd':
            coins = cells[current_cell - 1][1]
            new_gold = current_gold + coins
            new_dragons_killed = dragons_killed + [current_cell]
            if next_cell < n and cells[next_cell - 1][0] == 'p' and len(new_dragons_killed) >= cells[next_cell - 1][1]:
                backtrack(next_cell, current_gold, dragons_killed)  # Avoid killing the dragon if beauty level reached
            else:
                backtrack(next_cell, new_gold, new_dragons_killed)  # Continue with killing the dragon

    backtrack(1, 0, [])

    if len(dragons_to_kill) > 0:
        return max_gold, len(dragons_to_kill), dragons_to_kill
    else:
        return -1


if __name__ == "__main__":
    import subprocess

    # Make sure yaml package is installed
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
    import yaml

    parser = argparse.ArgumentParser(description="Process a YAML file containing parameters/inputs")
    parser.add_argument('yaml_file', type=str, help="Path to the YAML file containing parameters")
    inputs_file = parser.parse_args()

    data = read_yaml_file(inputs_file.yaml_file)
    result = calculate_max_gold(data)

    if result == -1:
        print(-1)
    else:
        max_gold, num_dragons, dragons_to_kill = result
        print(max_gold)
        print(num_dragons)
        print(dragons_to_kill)


