import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(-1,-2),-3)
    
    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)
    
    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
    
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
    
    def test_divide2(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
    
    def test_module1(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_module2(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()