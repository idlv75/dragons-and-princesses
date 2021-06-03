import unittest
import main


class TestCellInfo(unittest.TestCase):
    def setUp(self):
        self.cell1 = main.CellInfo(0, 2, 'd')
        self.cell2 = main.CellInfo(1, 2, 'p')
        self.cell3 = main.CellInfo(0, 3, 'p')

    def test_init(self):
        self.assertEqual(self.cell1.get_index(), 0)
        self.assertEqual(self.cell1.get_value(), 2)
        self.assertEqual(self.cell1.get_type(), 'd')

    def test_lt(self):
        self.assertTrue(self.cell1 < self.cell3)
        self.assertFalse(self.cell3 < self.cell1)
        self.assertFalse(self.cell1 < self.cell2)

    def test_gt(self):
        self.assertTrue(self.cell3 > self.cell1)
        self.assertFalse(self.cell1 > self.cell3)
        self.assertFalse(self.cell1 > self.cell2)

    def test_le(self):
        self.assertTrue(self.cell1 <= self.cell3)
        self.assertFalse(self.cell3 <= self.cell1)
        self.assertTrue(self.cell1 <= self.cell2)

    def test_ge(self):
        self.assertTrue(self.cell3 >= self.cell1)
        self.assertFalse(self.cell1 >= self.cell3)
        self.assertTrue(self.cell1 >= self.cell2)

    def test_eq(self):
        self.assertTrue(self.cell1 == self.cell2)
        self.assertFalse(self.cell1 == self.cell3)

    def test_ne(self):
        self.assertTrue(self.cell3 != self.cell1)
        self.assertFalse(self.cell1 != self.cell2)

    def test_copy(self):
        cell11 = self.cell1.copy()
        self.assertEqual(self.cell1.get_index(), cell11.get_index())
        self.assertEqual(self.cell1.get_value(), cell11.get_value())
        self.assertEqual(self.cell1.get_type(), cell11.get_type())

        cell11._index = 4
        self.assertNotEqual(self.cell1.get_index(), cell11.get_index())


if __name__ == '__main__':
    unittest.main()
