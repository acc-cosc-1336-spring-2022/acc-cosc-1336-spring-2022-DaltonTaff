<<<<<<< HEAD
from homework.d_repetition.repetition import get_factorial


get_factorial(4)
=======
import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function get_number.
'''
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers

class Test_Config(unittest.TestCase):
    def test_get_factorial(self):
        self.assertEqual(24, get_factorial(4))
        self.assertEqual(120, get_factorial(5))
        self.assertEqual(720,get_factorial(6))

    def test_sum_odd_numbers(self):
        self.assertEqual(16, sum_odd_numbers(7))
        self.assertEqual(25, sum_odd_numbers(9))
        self.assertEqual(25, sum_odd_numbers(10))
>>>>>>> bb0e719f575c0074fd908af7af32665434653d16
