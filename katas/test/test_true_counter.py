import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):

    def test_true_counter(self):
        self.assertEqual(count_true_values([True,True,True,True,False,True,False]),5)

    def test_one_true(self):
        self.assertEqual(count_true_values([True]),1)

    def test_one_flase(self):
        self.assertEqual(count_true_values([False]),0)

    def test_empty_list(self):
        self.assertEqual(count_true_values([]),0)

    def test_number_list(self):
        self.assertEqual(count_true_values([1,5,0,8,1,1,1,2,10]),4)

    
        
 
    
