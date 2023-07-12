from week_5 import rearrenge_name, validate_user
import unittest

class TestRearrange (unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrenge_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrenge_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrenge_name(testcase), expected)
    
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrenge_name(testcase), expected)

class TestValidateUser (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invaliduser", 1), False)

    def test_invalid_minlen(self):
        self.asserrtRaises(ValueError, validate_user, "user", -1)
    
    
unittest.main()
