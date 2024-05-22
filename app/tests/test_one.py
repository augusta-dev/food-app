# tests/test_calc.py

import unittest
from calc import add

class TestCalc(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=1)
        self.assertAlmostEqual(add(-1.1, 1.1), 0.0, places=1)
        self.assertAlmostEqual(add(-1.1, -1.1), -2.2, places=1)

    def test_add_strings(self):
        self.assertEqual(add('a', 'b'), 'ab')

if __name__ == '__main__':
    unittest.main()

#Use unittest.mock and MagicMock.Mock to mock tests to prevent us from running tests we dont need to run
#The Testing Web Requests video is really important
#Common test issues:
#Indentation, missing the test_ prefix, missing the self argument, missing the assert statement, missing the __name__ == '__main__' block, import error because of having both the test directory and the test module