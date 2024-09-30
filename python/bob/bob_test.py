# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/bob/canonical-data.json
# File last updated on 2023-07-20

import unittest
from bob import response  # Adjust this import based on your actual module and function names

class BobTest(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(response("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(response("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(response("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            response("Does this cryogenic chamber make me look fat?"), "Sure."
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(response("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(response("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(response("Hi there!"), "Whatever.")

if __name__ == '__main__':
    unittest.main()