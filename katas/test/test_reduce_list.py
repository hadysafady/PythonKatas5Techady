import unittest
from katas.reduce_list import reduce_array

class TestReduceList(unittest.TestCase):

    def test_reduce_list(self):
        self.assertEqual(reduce_array([5,8,9,1,0,2]),[5,3,1,-8,-1,2])

    def test_negative_list(self):
        self.assertEqual(reduce_array([-5,-10,-8,-4]),[-5,-5,2,4])

    def test_str(self):
        with self.assertRaises(TypeError):
            reduce_array(["f",'r',"asd",8])
    
    def test_empty_list(self):
        with self.assertRaises(IndexError):
            reduce_array([])

    def test_one_element(self):
        self.assertEqual(reduce_array([5]),[5])

    
