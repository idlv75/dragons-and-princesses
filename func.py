
import yaml


def dragons_and_prencesses(file_name):
    """
    dragons_and_prencesses calculates the dragons that should be killed, in order to get to the last princess.

    Parameters
    ----------
    file_name : yaml file, first element is the size
              last element is "p ?"
              and whats in between is either "p ?" or "d ?"
              ? is a random number.

    Returns
    -------
    -1 if there is no solution.
    else: maximum coins that the knight can collect.
          number of killed dragons.
          which dragons to kill.
    """
    with open(file_name) as parameters:
        dictYaml = yaml.safe_load(parameters)

    value_iterator = iter(dictYaml)
    first_value = next(value_iterator)
    journey = dictYaml[first_value]

    #jounrney = file_name
    journey_in_action = journey[1:]
    killed_dragons = []

    for index in range(len(journey_in_action)):
        x = journey_in_action[index].split(" ")

        if x[0] == "d":
            killed_dragons.append((index + 2, int(x[1])))

        if x[0] == "p" and index != (journey[0] - 2):
            while len(killed_dragons) >= int(x[1]):
                min_tup = min(killed_dragons, key=lambda t: t[1])
                killed_dragons.remove(min_tup)

        if index == (journey[0] - 2):
            if len(killed_dragons) < int(x[1]):
                return -1

    coins = sum([pair[1] for pair in killed_dragons])
    dragons = ""
    for tuple in killed_dragons:
        dragons += str(tuple[0]) + " "

    return str(coins) + "\n" + str(len(killed_dragons)) + "\n" + dragons
