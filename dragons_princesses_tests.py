import unittest
from dragons_princesses import parse_and_print_results
from dragons_princesses import read_parse_yaml_data


class MainTestClass(unittest.TestCase):
    def test_parse_and_print_results_good(self):
        dragons_array = [('12', 3), ('1', 5)]
        dragons_ammount_to_kill = 2
        res = parse_and_print_results(dragons_array, dragons_ammount_to_kill)
        self.assertEqual(res, True)

    def test_parse_and_print_results_bad(self):
        dragons_array = [('12', 3), ('1', 5)]
        dragons_ammount_to_kill = 3
        res = parse_and_print_results(dragons_array, dragons_ammount_to_kill)
        self.assertEqual(res, False)

    def test_read_parse_yaml_data(self):
        with self.assertRaises(Exception):
            read_parse_yaml_data("broken_path")

    def test_first_scenario(self):
        queue = find_path("input1.yaml")
        self.assertEqual(len(queue), 2)
        cells_list = [3, 5]
        dragons_cells = [obj.cell_number for obj in queue]
        self.assertListEqual(cells_list, dragons_cells)
    #
    # def test_second_scenario(self):
    #     queue = find_path("input1.yaml")
    #     self.assertEqual(sum(int(x.coins) for x in queue), 13)


if __name__ == "__main__":
    unittest.main()
