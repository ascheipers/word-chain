import unittest

from word_chain import word_chain, NoChainException


class TestWordChain(unittest.TestCase):

    def test_working_chain(self):
        pass

    def test_shortest_path(self):
        start_word = "same"
        end_word = "cost"
        dict_words = ["same", "fame", "some", "pome", "pose", "post", "cost", "lost", "came", "case", "cast"]

        self.assertEqual(len(word_chain(start_word, end_word, dict_words)), 5)

    def test_no_chain(self):
        start_word = "same"
        end_word = "cost"
        dict_words = ["same", "fame", "some", "pose", "post", "cost", "case", "cast"]

        self.assertRaises(NoChainException, word_chain, start_word, end_word, dict_words)
