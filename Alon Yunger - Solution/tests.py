import unittest
from dragons_and_princesses import dragons_and_princesses
import yaml
import random

# Contains a simple test that generates a random YAML file according to what the algorithm expects and runs it
class TestDragonsAndPrincesses(unittest.TestCase):
    
    def test_r(self):
        self.num_of_steps_possible = 2 * 10**5
        self.max_num_of_gold_per_dragon = 10**4
        self.max_dragons_slayed_per_princess = 2 * 10**5
        self.step_types = ["p", "d"]
        self.num_of_tests = 0
        
        num_of_steps = random.randint(2, self.num_of_steps_possible)
        
        # A dictionary to hold all steps and their number to later dump into a YAML file for test
        dict_to_store = {'number_of_steps' : num_of_steps}
        
        for i in range(1, num_of_steps):
            step_char = "p"
            if i < num_of_steps - 1:
                step_char = self.step_types[random.randint(0, len(self.step_types) - 1)]
                
            step_val = random.randint(1, self.max_dragons_slayed_per_princess)
            
            if step_char == self.step_types[1]:
                step_val = random.randint(1, self.max_num_of_gold_per_dragon)
            
            dict_to_store[i] = f'{step_char} {step_val}'
        
        file_name = f'test{self.num_of_tests}.yaml'
        
        with open(file_name, 'w') as outfile:
            yaml.dump(dict_to_store, outfile, default_flow_style=False)
            
        self.num_of_tests = self.num_of_tests + 1
        
        self.assertEqual(dragons_and_princesses(file_name), "-1")
    
    
if __name__ == '__main__':
    unittest.main()