import sys


# Read inputs file
def read_file(file_path):
    with open(file_path) as file:
        return file.readlines()


# Provide file as argument
if len(sys.argv) < 2:
    print("Please provide file as argument")
    exit()

yaml_file = sys.argv[1]
cells = read_file(yaml_file)
number_of_cells = int(cells[0])
counter = 1
dragon_dict = {}
is_married = False
#
for cell in cells[1:]:
    (cell_type, value) = cell.split(" ")
    value = int(value)
    if cell_type == "d":
        # value is gold
        # we kill the dragon here
        dragon_dict[str(counter + 1)] = value
    if cell_type == "p":
        # value is beauty
        dragons_killed = len(dragon_dict.values())
        if dragons_killed >= value:
            if counter != (number_of_cells - 1):
                # this is not the last princess we need to undo dragon kills
                while len(dragon_dict.values()) >= value:
                    dragon_to_unkill = min(dragon_dict, key=dragon_dict.get)
                    del dragon_dict[dragon_to_unkill]
            else:
                # we got married!
                is_married = True
    counter += 1
# Print the values
if is_married:
    print(sum(dragon_dict.values()))
    print(len(dragon_dict.values()))
    print(' '.join(dragon_dict.keys()))
else:
    print(-1)
