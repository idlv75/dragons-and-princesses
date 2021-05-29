import heapq
import yaml
import sys


def read_yaml(input_path):
    with open(input_path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


class Dragon:

    def __init__(self, index, gold):
        self.index = index
        self.gold = gold

    def __lt__(self, other):
        return self.gold < other.gold

    def __add__(self, other):
        return self.gold + other

    def __radd__(self, other):
        return self.__add__(other) if other else self


class DragonsAndPrincesses:

    def __init__(self, input_path):
        data = read_yaml(input_path)
        self._characters = data['characters']
        self._map_size = data['size']
        self._killed_dragons = []

    def dragons_and_princesses(self):
        for ind, character in enumerate(self._characters):
            character_type, value = character.split()
            try:
                value = int(value)
            except ValueError:
                raise ValueError("second value should be integer. for example: 'd 12'")
            if (ind + 2) == self._map_size:
                break
            if character_type == 'd':
                heapq.heappush(self._killed_dragons, Dragon(ind + 2, value))
            else:
                if len(self._killed_dragons) >= value:
                    value = len(self._killed_dragons) - value + 1
                    while value:
                        heapq.heappop(self._killed_dragons)
                        value -= 1
        self.print_results(value)

    def print_results(self, value):
        if len(self._killed_dragons) < value:
            print(-1)
        else:
            indexes_bool = [False] * (self._map_size + 1)
            gold_sum = sum(self._killed_dragons)
            killed = len(self._killed_dragons)
            while self._killed_dragons:
                d = heapq.heappop(self._killed_dragons)
                indexes_bool[d.index] = True
            print(gold_sum)
            print(killed)
            print(*[index for index, val in enumerate(indexes_bool) if val])


if __name__ == "__main__":
    DragonsAndPrincesses(sys.argv[1]).dragons_and_princesses()
