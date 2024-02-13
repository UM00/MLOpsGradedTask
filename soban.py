import unittest
import math

def factorial(n):
    """
    Compute the factorial of a non-negative integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class TestFactorialFunction(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 362880)
        self.assertEqual(factorial(20), math.factorial(20))  # Compare with math.factorial for validation

if __name__ == '__main__':
    unittest.main()
