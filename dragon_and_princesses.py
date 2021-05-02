#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math
import argparse
import os.path


def get_key(val,some_dict):
    for key, value in some_dict.items():
        if val == value:
            return key

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help="path_to_yaml_file",required=True)
args = parser.parse_args()
path_to_yaml_file = args.file

if not str(path_to_yaml_file).endswith(".yaml"):
    print("Error suffix isn't  .yaml")
    exit()


if not os.path.isfile(path_to_yaml_file):
    print("File doesn't exist")
    exit()

yaml_file = open(path_to_yaml_file, 'r')
# reading yaml file
lines = yaml_file.readlines()
num_of_cells = lines[0]
num_of_cells = int(num_of_cells)
min_cell_value = 2
max_cell_value = 2 * math.pow(10,5)

# input rules
if not isinstance(num_of_cells,int) and not  min_cell_value <= num_of_cells <= max_cell_value:
    print("Error: the first setence must contain an integer with the following rule: 2 ≤ n ≤ 2·(10^5)")
    exit()
if len(lines) != num_of_cells:
    print("Error: the number of cells not equal to the number of lines")
    exit()
if not lines[-1].startswith('p'):
    print("Error: last line must contain princess")
    exit()

amount_of_princess = [line.rstrip() for line in lines if "p" in line]
marriage = False
dict_of_cells = {}
counter = 0
for cell in lines:
        counter += 1
        if cell.startswith('d'):
            dict_of_cells[str(counter)] = int(cell.rstrip().split()[1])
        if cell.startswith('p'):
            beauty = cell.split()[1]
            if len(dict_of_cells.values()) and counter == len(lines):
                marriage = True
                print(sum(dict_of_cells.values()))
                print(len(dict_of_cells.values()))
                print(' '.join(dict_of_cells.keys()))
            while len(dict_of_cells.values()) >= int(beauty):
                key_to_remove = get_key(min(dict_of_cells.values()), dict_of_cells)
                del dict_of_cells[key_to_remove]

if marriage is False:
        print("-1")

