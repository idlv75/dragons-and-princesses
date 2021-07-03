import subprocess, os, sys
import heapq
import yaml


class yaml_data:
    def __init__(self, num_of_lines, knight_steps):
        self.num_of_lines = num_of_lines
        self.ammount_of_cells = num_of_lines - 1
        self.knight_steps = knight_steps
        self.dragons_to_kill = int(knight_steps[self.ammount_of_cells - 1].split()[1])


def install_project_requirements():
    print("making sure all project requirements installed.")
    try:
        import yaml
        print("all good.")
    except Exception as e:
        print("yaml libary not exists , installing.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", '-r', 'requirements.txt'])


def read_parse_yaml_data(file_path):
    print("Reading the yaml content")
    if os.path.isfile(file_path):
        with open(file_path) as file:
            steps_data = yaml.load(file, Loader=yaml.FullLoader)
            parsed_data = yaml_data(steps_data["array_cells_len"], steps_data["array_cells"])

            return parsed_data.__getattribute__("knight_steps"), \
                   parsed_data.__getattribute__("ammount_of_cells"), \
                   parsed_data.__getattribute__("dragons_to_kill")
    else:
        raise FileNotFoundError("Provided file was broken")


def parse_and_print_results(dragons_array, dragons_ammount_to_kill):
    if len(dragons_array) < int(dragons_ammount_to_kill):
        return False

    index_str = []
    coins_sum = 0
    for array_element in dragons_array:
        index_str.append(str(array_element[1]))
        coins_sum += int(array_element[0])
    print(coins_sum)
    print(len(dragons_array))
    print(" ".join(index_str))
    return True


def find_possible_path(knight_steps_var, amount_of_cells_var):
    # between each 2 princes we check the amount of dragons and match the required princess beauty to not marry her.
    dragons_array = []
    loop_index = 2
    for knight_step in knight_steps_var[:amount_of_cells_var - 1]:
        cell_type, cell_value = knight_step.split()
        if cell_type == "d":
            dragons_array.append((cell_value, loop_index))
        else:
            heapq.heapify(dragons_array)
            while len(dragons_array) >= int(cell_value):
                # remove min value
                heapq.heappop(dragons_array)
        loop_index += 1
    return dragons_array


if __name__ == '__main__':
    # provide path to file here , instructions not so clear about how file should passed.
    file_path = "steps_input_good.yaml"
    install_project_requirements()
    knight_steps, amount_of_cells, dragons_to_kill = read_parse_yaml_data(file_path)
    dragons_array_result = find_possible_path(knight_steps, amount_of_cells)
    test_result = parse_and_print_results(dragons_array_result, dragons_to_kill)
    if not test_result:
        print(-1)
