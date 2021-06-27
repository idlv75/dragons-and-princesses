from solution import find_path
import unittest

class SolutionTestCase(unittest.TestCase):

    def test_first_scenario(self):
        queue = find_path("input1.yaml")
        self.assertEqual(len(queue), 2)
        cells_list = [3, 5]
        dragons_cells = [obj.cell_number for obj in queue]
        self.assertListEqual(cells_list, dragons_cells)

    def test_second_scenario(self):
        queue = find_path("input1.yaml")
        self.assertEqual(sum(int(x.coins) for x in queue), 13)



if __name__ == "__main__":
    unittest.main()
