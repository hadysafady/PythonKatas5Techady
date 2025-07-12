import unittest
from katas.word_count import count_words

class TestWordCount(unittest.TestCase):

    def test_word_counter(self):
        self.assertEqual(count_words("next weak I'll go to the beach!"),7)

    def test_words_with_numbers(self):
        self.assertEqual(count_words("my weight is 87 kilograms"),4)

    def test_only_numbers(self):
        self.assertEqual(count_words("4515 28 844"),0)

    

    