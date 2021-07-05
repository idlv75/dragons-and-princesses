import unittest
import main


class test(unittest.TestCase):

    def test_1(self):
        length = 6
        cells = [('d', 10), ('d', 12), ('p', 2), ('d', 1), ('p', 2)]

        res_val = 13
        res_dragon_killed = 2
        res_idx_list = [3, 5]

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans[0])
        self.assertEqual(res_dragon_killed, ans[1])
        self.assertEqual(res_idx_list, ans[2])

    def test_2(self):
        length = 6
        cells = [('d', 10), ('d', 12), ('p', 2), ('d', 1), ('p', 3)]

        res_val = -1

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans)

    def test_3(self):
        length = 9
        cells = [('d', 10), ('d', 18), ('p', 2), ('d', 15), ('d', 25), ('p', 3), ('d', 1), ('p', 3)]

        res_val = 44
        res_dragon_killed = 3
        res_idx_list = [3, 6, 8]

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans[0])
        self.assertEqual(res_dragon_killed, ans[1])
        self.assertEqual(res_idx_list, ans[2])

    def test_4(self):
        length = 11
        cells = [('p', 5), ('p', 2), ('d', 10), ('d', 18), ('p', 2), ('d', 15), ('d', 25), ('p', 3), ('d', 1), ('p', 3)]

        res_val = 44
        res_dragon_killed = 3
        res_idx_list = [5, 8, 10]

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans[0])
        self.assertEqual(res_dragon_killed, ans[1])
        self.assertEqual(res_idx_list, ans[2])

    def test_5(self):
        length = 11
        cells = [('d', 105), ('p', 2), ('d', 10), ('d', 18), ('p', 2), ('d', 115), ('d', 25), ('p', 3), ('d', 1),
                 ('p', 3)]

        res_val = 221
        res_dragon_killed = 3
        res_idx_list = [2, 7, 10]

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans[0])
        self.assertEqual(res_dragon_killed, ans[1])
        self.assertEqual(res_idx_list, ans[2])

    def test_6(self):
        length = 6
        cells = [('d', 10), ('d', 12), ('p', 2), ('d', 1), ('p', 8)]

        res_val = -1

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans)

    def test_7(self):
        length = 8
        cells = [('d', 10), ('d', 12), ('p', 2), ('d', 1), ('d', 1), ('d', 1), ('p', 3)]

        res_val = 15
        res_dragon_killed = 4
        res_idx_list = [3, 5, 6, 7]

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans[0])
        self.assertEqual(res_dragon_killed, ans[1])
        self.assertEqual(res_idx_list, ans[2])

    def test_8(self):
        length = 22
        cells = [('d', 6), ('d', 1), ('d', 1024), ('d', 19), ('d', 1024), ('d', 29),
                 ('d', 12), ('p', 8), ('d', 102), ('d', 212), ('d', 512), ('d', 1024),
                 ('p', 5), ('d', 16), ('d', 10), ('p', 6), ('d', 100), ('d', 100), ('d', 100), ('d', 100),
                 ('p', 9)]

        res_val = 4000
        res_dragon_killed = 9
        res_idx_list = [4, 6, 12, 13, 15, 18, 19, 20, 21]

        ans = main.dragonsAndPrincesses((length, cells))
        self.assertEqual(res_val, ans[0])
        self.assertEqual(res_dragon_killed, ans[1])
        self.assertEqual(res_idx_list, ans[2])


if __name__ == '__main__':
    unittest.main()
