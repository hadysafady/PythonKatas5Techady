import unittest
from katas.matrix_rotate import rotate_matrix

class TestMatrixRotate(unittest.TestCase):
    
    def test_matrix_rotate(self):
        self.assertEqual(rotate_matrix([[10, 20, 30],[40, 50, 60],[70, 80, 90]]),[[70,40,10],[80,50,20],[90,60,30]] )

    def test_4x4matrix(self):
        self.assertEqual(rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]),[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]])

    
