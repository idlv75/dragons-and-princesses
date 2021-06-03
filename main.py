import heapq


# The class represents a cell in the map.
class CellInfo:
    _index = 0
    _value = 0
    _cell_type = 'p/d'

    # A contractor that gets all the class's data members.
    def __init__(self, index, value, cell_type):
        self._index = index
        self._value = value
        self._cell_type = cell_type

    # Creates a deep copy of the CellInfo.
    def copy(self):
        return CellInfo(self.get_index(), self.get_value(), self.get_type())

    # Return the CellInfo's index - place in the map.
    def get_index(self):
        return self._index

    # Return the CellInfo's value - number of coins for a dragon,
    # and number of dragons to kill in order to marry the princess for a princess.
    def get_value(self):
        return self._value

    # Return the CellInfo's type (d for dragon, p for princess).
    def get_type(self):
        return self._cell_type

    # Overloads the operator <, Compare between the two CellInfo's values.
    def __lt__(self, other):
        return self.get_value() < other.get_value()

    # Overloads the operator >, Compare between the two CellInfo's values.
    def __gt__(self, other):
        return self.get_value() > other.get_value()

    # Overloads the operator >=, Compare between the two CellInfo's values.
    def __le__(self, other):
        return self.get_value() <= other.get_value()

    # Overloads the operator >=, Compare between the two CellInfo's values.
    def __ge__(self, other):
        return self.get_value() >= other.get_value()

    # Overloads the operator ==, Compare between the two CellInfo's values.
    def __eq__(self, other):
        return self.get_value() == other.get_value()

    # Overloads the operator !=, Compare between the two CellInfo's values.
    def __ne__(self, other):
        return self.get_value() != other.get_value()


class DragonAndPrincesses:
    _cell_array = []

    # A contractor, initiates the class data members.
    def __init__(self):
        self._cell_array = []

    # Fills the class's cell_array with the cell_map the function gets.
    def set_map(self, cell_map):
        self._cell_array = []
        for cell in cell_map:
            self._cell_array.append(cell.copy())

    # Fills the class's cell_array with data from the user.
    def get_map_from_input(self):
        cell_nums = int(input())

        for i in range(cell_nums - 1):
            line = input()
            line = line.split(' ')
            cell_type = line[0]
            value = int(line[1])
            cell = CellInfo(i, value, cell_type)
            self._cell_array.append(cell)

    # Fills the class's cell_array with data from a file. The function gets the file's name as a parameter.
    def get_map_from_file(self, file_name):
        file = open(file_name)
        cell_nums = int(file.readline())

        for i in range(cell_nums - 1):
            line = file.readline()
            line = line.split(' ')
            cell_type = line[0]
            value = int(line[1])
            cell = CellInfo(i, value, cell_type)
            self._cell_array.append(cell)

        file.close()

    # The function solve the map, and returns a string represents the solution.
    def solution(self):
        dragons_from_last_princess = []
        dragons_to_kill = []

        # Goes throughout the map.
        for cell in self._cell_array:
            # If there is a dragon in the current cell.
            if cell.get_type() == 'd':
                new_cell = CellInfo(cell.get_index(), -cell.get_value(), cell.get_type())
                dragons_from_last_princess.append(new_cell)
            # If there is a princess in the current cell.
            elif cell.get_type() == 'p':
                # Heapify the list of dragons the knight met after he had passed the last princess.
                heapq.heapify(dragons_from_last_princess)

                dragon_index = 0
                new_dragons_to_kill = []

                # Goes until the number of dragons the knight can kill without marring the princess.
                # (At the last cell, the loop continues until there are nmo dragons left.)
                end_of_range = cell.get_value() - 1
                if cell.get_index() == len(self._cell_array) - 1:
                    end_of_range = len(dragons_to_kill) + len(dragons_from_last_princess)
                for i in range(end_of_range):
                    # If there are no more dragons in the list contains the dragons appeared before the last princess.
                    # Or there are no more dragons in the list contains the dragons appeared after the last princess.
                    if dragon_index >= len(dragons_to_kill) or len(dragons_from_last_princess) == 0:
                        break
                    # Using <= instead of >= because the algorithm works with min-heap
                    # and searches for the maximum value.
                    if dragons_to_kill[dragon_index].get_value() < (dragons_from_last_princess[0].get_value()):
                        new_dragons_to_kill.append(dragons_to_kill[dragon_index].copy())
                        dragon_index = dragon_index + 1
                    else:
                        new_dragon = heapq.heappop(dragons_from_last_princess).copy()
                        new_dragons_to_kill.append(new_dragon)

                if dragon_index >= len(dragons_to_kill):
                    for i in range(len(new_dragons_to_kill), end_of_range):
                        if len(dragons_from_last_princess) == 0:
                            break
                        new_dragon = heapq.heappop(dragons_from_last_princess).copy()
                        new_dragons_to_kill.append(new_dragon)
                elif len(dragons_from_last_princess) == 0:
                    for i in range(len(new_dragons_to_kill), end_of_range):
                        if dragon_index >= len(dragons_to_kill):
                            break
                        new_dragons_to_kill.append(dragons_to_kill[dragon_index].copy())
                        dragon_index = dragon_index + 1

                dragons_to_kill = new_dragons_to_kill
                dragons_from_last_princess = []

        # Check the requirements of the last princess
        if len(dragons_to_kill) < self._cell_array[len(self._cell_array) - 1].get_value():
            return -1

        coins_num = 0
        dragons_indexes = ""
        dragons_to_kill = sorted(dragons_to_kill, key=CellInfo.get_index)
        for dragon in dragons_to_kill:
            # The number of gold coins in the InfoCells is negative(a min-heap was used).
            coins_num -= dragon.get_value()
            dragons_indexes += str(dragon.get_index() + 2) + " "

        sol = str(coins_num) + "\n" + str(len(dragons_to_kill)) + "\n" + dragons_indexes
        return sol


def main():
    dap = DragonAndPrincesses()
    dap.get_map_from_file("input.txt")
    print(dap.solution())


if __name__ == '__main__':
    main()
