import sys
import argparse
import os
import yaml

# const
MAX_NUMBER_OF_CELLS = 200000
MIN_NUMBER_OF_CELLS = 1
MAX_NUMBER_OF_COINS = 10000
PRINCESS = 'p'
DRAGON = 'd'

def cast_to_int(var: str) -> int:
    """
    this func will cast input to int and checks that input is in valid range
    :param var: input that need to cast to int
    :return: in case of success, casted int
             in case of failure, program will exit with 1
    """
    try:
        var = int(var)
        if var < MIN_NUMBER_OF_CELLS or var > MAX_NUMBER_OF_CELLS:
            raise Exception
    except:
        print(f"invalid input {var}")
        sys.exit(1)

    return var

def parse_input_data(input_data: list) -> list:
    """
    this func receives input data from yaml file and returns list of cells
    :param input_data: list from yaml file
    :return: list of cells, where first item is number of cells and other are tuples:
             d, num of coins or p, beauty range
    """
    cells = []
    for item in input_data:
        if len(cells):
            # this is not the first cell, append tuple
            a, b = item.split()
            cells.append((a, cast_to_int(b)))
        else:
            # this is the first cell, append int
            n = cast_to_int(item)
            cells.append(n)

    return cells

def get_princess_and_coins (n: int, cells: list, coins: int, defeated_dragons: int, i: int, drgns_lst = None) -> tuple:
    """
    :param n: (int) the number of cells
    :param cells: (list) of cells
    :param coins: (int) number of collected gold coins
    :param defeated_dragons: (int) number of defeated dragons
    :param i: (int) index of the current cell
    :param drgns_lst: (list of int) list of defeated dragons' cells

    :return: in case of success: returns number of collected gold coins, number of defeated dragons,
                                 and list of defeated dragons' cells
             in case of failure: -1,0,None
    """
    if drgns_lst == None:
        drgns_lst = []

    # stop condition, we're in the last cell
    if n == i:
        if cells[i-1][0] == PRINCESS and cells[i-1][1] <= defeated_dragons:
            return coins, defeated_dragons, drgns_lst
        else:
            return -1, 0, None

    # cell with princess
    if cells[i-1][0] == PRINCESS:
        if cells[i-1][1] <= defeated_dragons:
            return -1, 0, None
        else:
            return get_princess_and_coins(n, cells, coins, defeated_dragons, i + 1, drgns_lst)

    # cell with dragon
    elif cells[i-1][0] == DRAGON:
        # check validity of coins number
        if cells[i-1][1] > MAX_NUMBER_OF_COINS:
            print(f"too much coins in cell number {i}")
            sys.exit(1)

        d_l1 = drgns_lst.copy()
        # defeat dragon, take his coins and add him to list of defeated dragons
        d_l1.append(i)
        res1 = get_princess_and_coins(n, cells, coins+cells[i-1][1], defeated_dragons+1, i+1, d_l1)

        # pass through the dragon without fight
        res2 = get_princess_and_coins(n, cells, coins, defeated_dragons, i+1, drgns_lst)

        # choose path with max coins
        return max(res1,res2)

    else:
        print(f"invalid input in cell number {i}")
        sys.exit(1)

def parse_args() -> str:
    """
    check required argument is valid and passed parsing argument
    :return: path to existed yaml input file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-yml', '--yaml-file', type=str, required=True, help="Path to yaml file")
    args = parser.parse_args()

    # check file exists
    if not os.path.exists(args.yaml_file):
        print(f"there is no such file {args.yaml_file}")
        sys.exit(1)

    return args.yaml_file

if __name__ == "__main__":
    # parsing input
    input_file = parse_args()
    try:
        with open(input_file, 'r') as stream:
            input_data = yaml.safe_load(stream)
            cells = parse_input_data(input_data)
    except Exception as e:
        print(f"error while opening file {parse_args.yaml_file}")
        print(e)
        sys.exit(1)

    # length check
    n = cells[0]
    if len(cells) != n:
        print(f"invalid number of cells: {n} instead {len(cells)}")
        sys.exit(1)

    # check that there is a princess in the last cell
    if cells[n-1][0] != PRINCESS:
        print("there is no princess in last cell")
        sys.exit(1)

    res = get_princess_and_coins(n, cells, coins=0, defeated_dragons=0, i=2)

    if res[0] > 0:
        # success
        print(f"{res[0]}\n{res[1]}\n{' '.join(str(d) for d in res[2])}")
    else:
        # no valid path was found
        print(-1)