import unittest
from katas.time_me import measure_execution_time, quick_function, sample_function

class TestMeasureExecutinTime(unittest.TestCase):

    def test_sample_function(self):
        thefunc = measure_execution_time(sample_function)
        self.assertLessEqual(thefunc,0.555)
    
    def test_quick_function(self):
        thefunc=measure_execution_time(quick_function)
        self.assertLessEqual(thefunc,0.001)

    def test_error(self):
        with self.assertRaises(TypeError):
            measure_execution_time("sad356asd")

    def test_floating(self):
        with self.assertRaises(TypeError):
            measure_execution_time(measure_execution_time(quick_function))

        




    