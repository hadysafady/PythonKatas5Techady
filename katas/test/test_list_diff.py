import unittest 
from katas.list_diff import find_difference

class TestListDiff(unittest.TestCase):
    def test_list_diff(self):
        self.assertEqual(find_difference([0,5,7,9,10,30.2]),30.2)
    
    def test_negative_numbers(self):
        self.assertEqual(find_difference([-8,-9,-20,1,0]),21)
    
    def test_single_element(self):
        self.assertEqual(find_difference([7]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
           find_difference([])

if __name__ == '__main__':
    unittest.main()