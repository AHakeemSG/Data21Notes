# Unit test for calculator

from simple_calc import SimpleCalc
import unittest
import pytest  # to install pytest use in terminal: pip install -U pytest
                # -U gives us the latest update
                # -v gives us the details of the tests that are running


# we have to use TestCase as an argument because it will have all our testing. We will inherit its attributes
class Calctests(unittest.TestCase):
    calc = SimpleCalc()

    # put in parameter 2, 4 and the 6 is confirming the output should be 6
    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    # parameter 4 and 2 will be subtracted to retrieve  the third argument, 2
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)


# pytest
