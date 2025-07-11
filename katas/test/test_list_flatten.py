import unittest 
from katas.list_flatten import flatten_list

class TestListFlatten(unittest.TestCase):
    
    def test_not_list(self):
       with self.assertRaises(TypeError):
           flatten_list("asasdsad")

    def test_normal_list(self):
        self.assertEqual(flatten_list([1,8,[5,6,8,9],2,[5,[8,[10,5]]],100]),[1,8,5,6,8,9,2,5,8,10,5,100])

    def test_list_with_chars(self):
        self.assertEqual(flatten_list([5,'a',[' ','d','=',5],-5,0]),[5,'a',' ','d','=',5,-5,0])
    
    def test_empty_list(self):
        self.assertEqual(flatten_list([]),[])
    
    def test_str_list(self):
        self.assertEqual(flatten_list(['pedri','yamal',['rafa','cubarsi'],'gavi']),['pedri','yamal','rafa','cubarsi','gavi'])
