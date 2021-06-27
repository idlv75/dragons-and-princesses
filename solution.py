import yaml
from operator import attrgetter

class Dragon:
    def __init__(self, cell_number, coins):
        self.cell_number = cell_number
        self.coins = coins

    def __str__(self):
        return "cell_number = {}, coins = {}".format(self.cell_number, self.coins)

class Dragons:

    target_value = 0
    def __init__(self):
        self.dragons_queue = []

    def remove_dragon(self):
        min_value_dragon = min(self.dragons_queue, key=attrgetter('coins'))
        self.dragons_queue.remove(min_value_dragon)

    def dragons_money(self):
        return sum(int(x.coins) for x in self.dragons_queue)

    def dragons_print(self):
        for dragon in self.dragons_queue:
            print(dragon)

def find_path(input_file):
    with open(input_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    dragons = Dragons()
    steps = data['steps']
    Dragons.target_value = steps.pop().split()[1]
    cell_num = 2
    summary_coins = 0
    for step in steps:
        type, value = step.split()
        if type == "d":
            dragon = Dragon(cell_num, value)
            dragons.dragons_queue.append(dragon)
            summary_coins += int(dragon.coins)
        else:
            while dragons and len(dragons.dragons_queue) >= int(value):
                dragons.remove_dragon()
        cell_num += 1

    if len(dragons.dragons_queue) < int(Dragons.target_value):
        print("-1")
    else:
        print (dragons.dragons_money())
        print (len(dragons.dragons_queue))
        for dragon in dragons.dragons_queue:
            print (dragon.cell_number, end= " ")
    return dragons.dragons_queue

if __name__ == '__main__':
    find_path('input1.yaml')




