import os
import unittest

TEST_DATA_FILENAME = os.path.join(os.path.dirname(__file__), 'input.yml')


class TestMain(unittest.TestCase):
    def test_yaml_input(self):
        with open(TEST_DATA_FILENAME, 'r', encoding='utf-8') as file:
            for idx, line in enumerate(file):

                data = line.split()
                self.assertIsNotNone(data)

                if idx == 0:
                    self.assertAlmostEqual(len(data), 2)
                else:
                    self.assertAlmostEqual(len(data), 3)

                if data[1] == "p":
                    self.assertNotAlmostEqual(int(data[2]), 0)
