'''
Solution to Dragons and Princesses
Coded in Python 2 !!!
'''


######################
# Imports
######################
import sys


######################
# Constants
######################
KNIGHT_CANT_MARRY_PRINCESS_OUTPUT = '-1'
MIN_BEAUTY = 1
MAX_BEAUTY = 2*10**5
MIN_NUM_OF_CELLS = 2
MAX_NUM_OF_CELLS = 2*10**5
MIN_NUM_OF_COINS = 1
MAX_NUM_OF_COINS = 10**4


# Extracting input
try:
    yaml_file_path = sys.argv[1]
except:
    raise Exception("Missing input file parameter")

if not yaml_file_path.endswith(".yaml"):
    raise Exception("Bad input error: input file must be yaml file")

try:
    input_file = open(yaml_file_path, 'r')
except:
    raise Exception("Couldn't open input file")

cells = input_file.readlines()
num_of_cells = len(cells)

# Validating input
if not cells[-1].startswith('p'):
    raise Exception("Bad input error: last line of input must begin with 'p'")
if num_of_cells > MAX_NUM_OF_CELLS or num_of_cells < MIN_NUM_OF_CELLS:
    raise Exception("Bad input error: first line of input must contain integer between 2 and 200,000")
if num_of_cells != len(cells):
    raise Exception("Bad input error: first line of input must be equal to the number of lines")

cells.pop(0)
# Initializations
current_cell = 1
slain_dragons = {}
'''
slain_dragons dictionary will include number of cell as key and amount of gold coins the dragon holds as value:
E.g:
{2: 14, 5: 8}
'''

for cell in cells:
    current_cell += 1
    if cell.startswith('d'):
        num_of_coins = int(cell.split()[1])
        if num_of_coins > MAX_NUM_OF_COINS or num_of_coins < MIN_NUM_OF_COINS:
            raise Exception("Bad input error: caught in line: {}. Amount of coins must be between 1 and 10,000".format(current_cell))
        # Adding cell to dictionary
        slain_dragons[str(current_cell)] = num_of_coins
    elif cell.startswith('p'):
        beauty = int(cell.split()[1])
        if current_cell == num_of_cells:
            if beauty > len(slain_dragons):
                print(KNIGHT_CANT_MARRY_PRINCESS_OUTPUT)
            else:
                slain_dragon_cells = " ".join(slain_dragons.keys())
                print("{}\n{}\n{}".format(sum(slain_dragons.values()), len(slain_dragons), slain_dragon_cells))
        else:
            while beauty <= len(slain_dragons):
                lowest_amount_of_coins = min(slain_dragons.values())
                for key, val in slain_dragons.items():
                    if val == lowest_amount_of_coins:
                        slain_dragons.pop(key)
    else:
        raise Exception("Bad input error: line number {} didn't begin with 'p' or 'd'".format(current_cell))
