import yaml
import sys

class dragons_and_princes():

    def __init__(self):

        self.killed_dragons = {}
        self.map_size = 0
        self.data = []
        self.marrige = 0


    def read_yml(self):
        """
        Read the yml file
        """
        flag = 1
        try:
            path = sys.argv[1]
        except Exception as e:
            print("Didnt put a file name")
            print(f'Exception has accured -> {e}')
            path = input("Enter yml file path -> ")

        while(flag):
            try:
                with open(path, 'r') as f:
                    self.data = yaml.safe_load(f)
                flag = 0
            except Exception as e:
                print(f'Exception has accured -> {e}')
                print("Try another file")
                path = input("Enter yml file path -> ")
            

    def parse(self):
        """
        Parse the data from the file
        """

        self.map_size = self.data[0]
        self.data = self.data[1:]
    
    def find_princes(self):
        """ 
        Start to walk and kill the correct amount of dragons to get the princes.
        """
        for index in range(len(self.data)):
            
            step = self.data[index].split(" ")
            
            if(step[0] == 'd'):
                self.killed_dragons[index] = step[1]
            
            elif(step[0] == 'p' and (index+2) != self.map_size):
                while(len(self.killed_dragons) >= int(step[1])):
                    min_val = min(self.killed_dragons, key=self.killed_dragons.get)
                    del self.killed_dragons[min_val]
            
            elif(len(self.killed_dragons) >= int(step[1])):
                self.marrige = 1

    def print_output(self):
        """ 
        Print the needed out put.
        First line - sum of coins.
        Second line - Amount of killed dragons
        Third line - Position of the dragons in the map
        """

        if(self.marrige == 1):
            print(sum([int(i) for i in self.killed_dragons.values()]))
            print(len(self.killed_dragons))
            print(sorted([x+2 for x in list(self.killed_dragons.keys())]))

        else:
            print( -1 )

    def play(self):

        self.read_yml()
        self.parse()
        self.find_princes()
        self.print_output()



def main():
    """
    The data I used in yaml files are:
    First one -> 
    6
    d 10
    d 12
    p 2
    d 1
    p 2

    Second ->
    6
    d 10
    d 12
    p 2
    d 1
    p 3
    
    """
    dragons_and_princes().play()



if __name__ == '__main__':
    main()