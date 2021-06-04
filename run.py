import fileinput
import queue
import sys
from dataclasses import dataclass, field


def main():
    find_match(parse_yaml())


def parse_yaml(file=None) -> []:
    if file is None:
        try:
            file = sys.argv[1]
        except Exception as e:
            print("No input file name after the executed script, Error:", e)
            return

    cells = []
    with fileinput.input(file) as lines:
        next(lines)
        for idx, line in enumerate(lines, start=2):
            data = line.split()
            if data[1] == "d":
                cells.append(Dragon(data[2], idx))
            else:
                cells.append(Princess(data[2]))
    return cells


def find_match(cells):
    if cells is not list:
        return

    dragons = queue.PriorityQueue()
    coins = 0
    positions = []

    for position, cell in enumerate(cells):

        if type(cell) is Dragon:
            dragons.put(cell)
            coins += int(cell.coins)
            positions.append(cell.position)

        if type(cell) is Princess:
            if position != (len(cells) - 1):
                while int(cell.beauty) <= dragons.qsize():
                    dragon = dragons.get()
                    coins -= int(dragon.coins)
                    positions.remove(dragon.position)
                else:
                    continue
            else:
                if int(cell.beauty) > dragons.qsize():
                    print(-1)
                    return
    print(coins, dragons.qsize(), sorted(positions), sep='\n')


@dataclass(order=True)
class Dragon:
    coins: int
    position: int = field(compare=False)


@dataclass
class Princess:
    beauty: int


if __name__ == '__main__':
    main()
