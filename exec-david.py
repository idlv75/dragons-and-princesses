import sys
import yaml

# Read input file
def read_file(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


# Provide file as argument
if len(sys.argv) < 2:
    print("Please provide file as argument")
    exit()

# Read input file as Yaml format
yaml_file = sys.argv[1]
input =  read_file(yaml_file)
number_of_cells = int(input["numberOfCells"])
counter = 1
dragon_dict = {}
is_married = False

# Check if princess gonna marry you
for cell in input['cells']:
    cell_type = cell['type']
    value = int(cell['value'])
    if cell_type == "D":
        # value is gold
        # we kill the dragon here
        dragon_dict[str(counter + 1)] = value
    if cell_type == "P":
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
    