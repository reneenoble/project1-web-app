# Create some python unit tests to test the functions in helper_functions.py

import unittest
from helper_functions import capitalise_name, get_colours, get_names_starting_with

class TestHelperFunctions(unittest.TestCase):
    def test_capitalise_name(self):
        self.assertEqual(capitalise_name("james"), "James")
        self.assertEqual(capitalise_name("fred"), "Fred")
        self.assertEqual(capitalise_name("sarah"), "Sarah")
        self.assertEqual(capitalise_name("jane"), "Jane")
        self.assertEqual(capitalise_name("joe"), "Joe")


    def test_get_colours(self):
        self.assertEqual(get_colours(3), ["red", "green", "blue"])
        self.assertEqual(get_colours(5), ["red", "green", "blue", "yellow", "black"])
        self.assertEqual(get_colours(8), ["red", "green", "blue", "yellow", "black", "white", "purple", "orange"])
        self.assertEqual(get_colours(1), ["red"])
        self.assertEqual(get_colours(0), [])
        self.assertEqual(get_colours(2), ["red", "green"])

    def test_get_names_starting_with(self):
        names = ["sally", "fred", "sarah", "jane", "joe"]
        self.assertEqual(get_names_starting_with(names, "j"), ["jane", "joe"])
        self.assertEqual(get_names_starting_with(names, "f"), ["fred"])
        self.assertEqual(get_names_starting_with(names, "s"), ["sally", "sarah"])
        self.assertEqual(get_names_starting_with(names, "a"), [])
        self.assertEqual(get_names_starting_with(names, "z"), [])
        self.assertEqual(get_names_starting_with(names, "j"), ["jane", "joe"])

# Run the tests
if __name__ == "__main__":
    unittest.main()
