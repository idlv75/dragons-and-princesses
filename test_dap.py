import unittest
import main


class TestDAP(unittest.TestCase):
    def test_file(self):
        dap = main.DragonAndPrincesses()
        dap.get_map_from_file("input.txt")
        sol = dap.solution()
        expt_sol = "13\n2\n3 5 "
        self.assertEqual(sol, expt_sol)

    def test_case1(self):
        map_array = [main.CellInfo(0, 10, 'd'),
                     main.CellInfo(1, 12, 'd'),
                     main.CellInfo(2, 2, 'p'),
                     main.CellInfo(3, 1, 'd'),
                     main.CellInfo(4, 2, 'p')]
        dap = main.DragonAndPrincesses()
        dap.set_map(map_array)
        sol = dap.solution()
        expt_sol = "13\n2\n3 5 "
        self.assertEqual(sol, expt_sol)

    def test_case2(self):
        map_array = [main.CellInfo(0, 10, 'd'),
                     main.CellInfo(1, 12, 'd'),
                     main.CellInfo(2, 2, 'p'),
                     main.CellInfo(3, 1, 'd'),
                     main.CellInfo(4, 3, 'p')]
        dap = main.DragonAndPrincesses()
        dap.set_map(map_array)
        sol = dap.solution()
        expt_sol = -1
        self.assertEqual(sol, expt_sol)

    def test_case3(self):
        map_array = [main.CellInfo(0, 10, 'd'),
                     main.CellInfo(1, 12, 'd'),
                     main.CellInfo(2, 2, 'p'),
                     main.CellInfo(3, 1, 'd'),
                     main.CellInfo(4, 2, 'p')]
        dap = main.DragonAndPrincesses()
        dap.set_map(map_array)
        sol = dap.solution()
        expt_sol = "13\n2\n3 5 "
        self.assertEqual(sol, expt_sol)

    def test_case4(self):
        map_array = [main.CellInfo(0, 10, 'd'),
                     main.CellInfo(1, 12, 'd'),
                     main.CellInfo(2, 3, 'p'),
                     main.CellInfo(3, 2, 'd'),
                     main.CellInfo(4, 2, 'p'),
                     main.CellInfo(5, 1, 'd'),
                     main.CellInfo(6, 2, 'p')]

        dap = main.DragonAndPrincesses()
        dap.set_map(map_array)
        sol = dap.solution()
        expt_sol = "13\n2\n3 7 "
        self.assertEqual(sol, expt_sol)

    def test_case5(self):
        map_array = [main.CellInfo(0, 10, 'd'),
                     main.CellInfo(1, 12, 'd'),
                     main.CellInfo(2, 3, 'p'),
                     main.CellInfo(3, 2, 'd'),
                     main.CellInfo(4, 2, 'p'),
                     main.CellInfo(5, 22, 'd'),
                     main.CellInfo(6, 23, 'd'),
                     main.CellInfo(7, 1, 'p')]

        dap = main.DragonAndPrincesses()
        dap.set_map(map_array)
        sol = dap.solution()
        expt_sol = "57\n3\n3 7 8 "
        self.assertEqual(sol, expt_sol)


if __name__ == '__main__':
    unittest.main()

