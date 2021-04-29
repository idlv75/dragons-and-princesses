"""

@author: Ranin Nassra

"""

from func import dragons_and_prencesses
import random
import yaml
import sys

"""
    I made an additional code to generate random list, 
    in order to use it just remove the comments. (line 54-55 in this file and in func.py line 30).
    and remove the file handling.

    
    When executing unit_test put the file name as an argument.
"""


def generate_random_list():
    """
    generate_random_list generates a random list of a random size n (2 ≤ n ≤ 2·10^5).

    Returns
    -------
    random_list: lists first element is the size of the list n(2 ≤ n ≤ 2·10^5).
                 each other element between 2 <= i < n contains eather a (dragon, coins) or  (princess, beauty).
                 coins = g (1 <= g <= 10^4)
                 beauty = b (1 <= b <= 2·10^5)
                 last element is a princess.
    """
    random_list = []

    size = random.randint(2, 2 * (pow(10, 5)))
    random_list.append(size)

    for i in range(size - 2):
        charachter = random.randint(0, 1)

        if charachter == 0:
            b = random.randint(1,  2 * (pow(10, 5)))
            random_list.append("p " + str(b))

        if charachter == 1:
            g = random.randint(1, (pow(10, 4)))
            random_list.append("d " + str(g))

    b = random.randint(1,  2 * (pow(10, 5)))
    random_list.append("p " + str(b))

    return random_list


if __name__ == "__main__":
   # journey = generate_random_list()
   # print("output: {}".format(dragons_and_prencesses(journey)))

    input_file = str(sys.argv[1])
    print("output:\n{}".format(dragons_and_prencesses(input_file)))
