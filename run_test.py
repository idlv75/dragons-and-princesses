import unittest
import princesses_and_dragons

# input vs expected output for testing
test0 = [6, ('d',10),('d',12),('p',2),('d',1),('p',2)]
output0 = (13, 2, [3,5])

test1 = [6, ('d',10),('d',12),('p',2),('d',1),('p',3)]
output1 = (-1, 0, None)

test2 = [8, ('d',10),('p',2),('p',2),('p',2),('p',2),('d',12),('p',2)]
output2 = (22, 2, [2,7])

# invalid input
test3  = [8,('d',20000)]

class TestStringMethods(unittest.TestCase):

    def test_0(self):
        self.assertEqual(princesses_and_dragons.get_princess_and_coins(test0[0],test0,0,0,2), output0)
    def test_1(self):
        self.assertEqual(princesses_and_dragons.get_princess_and_coins(test1[0],test1,0,0,2), output1)
    def test_2(self):
        self.assertEqual(princesses_and_dragons.get_princess_and_coins(test2[0],test2,0,0,2), output2)
    def test_3(self):
        with self.assertRaises(SystemExit) as cm:
            princesses_and_dragons.get_princess_and_coins(test3[0],test3,0,0,2)
        # it is expected to get sys.exit(1) here
        self.assertEqual(cm.exception.code, 1)

if __name__ == '__main__':
    unittest.main()