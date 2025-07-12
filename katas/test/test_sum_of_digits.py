import unittest 
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_sum_of_digits(self):
        self.assertEqual(sum_of_digits("asd58sad4"),17)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("What's your name?"),0)
    
    def test_ignoring_float_and_neg_numbers(self):
        self.assertEqual(sum_of_digits("-1.0 degree and -5"),6)

    def test_not_string(self):
        with self.assertRaises(TypeError):
            sum_of_digits(45622)

    


    

    

    