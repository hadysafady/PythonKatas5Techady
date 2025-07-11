import unittest
from katas.longest_common_prefix import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):

    def test_longest_prefix(self):
        self.assertEqual(longest_common_prefix(["ardew","ardeeewq","ardelkmn"]),"arde")

    def test_numbers(self):
        with self.assertRaises(TypeError):
            longest_common_prefix(["home", 5 , "homeland"])

    def test_sensitive_char(self):
        self.assertEqual(longest_common_prefix(["alfa","Alone","albania"]),"")

    