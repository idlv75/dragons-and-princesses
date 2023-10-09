import omri_dragons_and_princesses  
import unittest
import yaml

# Load parameters from parameters.yaml
with open('parameters.yaml', 'r') as file:
    parameters1 = yaml.safe_load(file)

# Load parameters from parameters2.yaml
with open('parameters2.yaml', 'r') as file:
    parameters2 = yaml.safe_load(file)

class TestScript(unittest.TestCase):

    def test_with_parameters1(self):
        result = omri_dragons_and_princesses.calculate_max_gold(parameters1)
        self.assertEqual(result, (13, 2, [2, 4]))  
        print(result)
    def test_with_parameters2(self):
        result = omri_dragons_and_princesses.calculate_max_gold(parameters2)
        self.assertEqual(result, -1)  
        print(result)

if __name__ == '__main__':
    unittest.main()


