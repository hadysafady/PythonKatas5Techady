import unittest
from unittest.mock import Mock
from katas.do_n_times import do_n_times

class TestDoNTimes(unittest.TestCase):
    def test_do_n_times(self):
        mock_func = Mock()
        do_n_times(mock_func,4)
        self.assertEqual(mock_func.call_count,4)
    
    def test_zero_times(self):
        mock_func=Mock()
        do_n_times(mock_func,0)
        self.assertEqual(mock_func.call_count,0)
    
    def test_invalidfunc(self):
        with self.assertRaises(TypeError):
            do_n_times( "shalom" ,6)
        






