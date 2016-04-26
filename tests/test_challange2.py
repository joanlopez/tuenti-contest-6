from unittest import TestCase
from src.challenge2.main import *


class TestChallange2(TestCase):
    def test_that_reading_correctly_words_from_file(self):
        words = get_words_from_text_file("testCorpus.txt")
        self.assertEquals(["Blue", "White", "Aqua", "Azure", "Beige", "Lavender"], words)

    def test_that_getting_the_right_effective_words(self):
        words = ["Blue", "White", "Aqua", "Azure", "Beige", "Lavender"]
        effective_words = get_effective_words(words, 1, 3)
        self.assertEquals(["Blue", "White", "Aqua"], effective_words)

    def test_that_most_frequency_returns_the_right_words(self):
        words = ["Blue", "White", "Blue", "White", "Beige", "Lavender", "Blue"]
        most_frequency_words = get_most_frequency_words(words, 2)
        self.assertEquals(2, len(most_frequency_words))
        self.assertEquals("Blue", most_frequency_words[0][0])
        self.assertEquals(3, most_frequency_words[0][1])
        self.assertEquals("White", most_frequency_words[1][0])
        self.assertEquals(2, most_frequency_words[1][1])

