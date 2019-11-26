# Isaac Krementsov
# 11/25/19
# List Manipulator Test - Test cases for the ListManipulator class methods

import unittest


# Test the ListManipulator's min method with a variety of inputs
class TestListManipulatorMin(unittest.TestCase):
    # Test the min method with a list containing more than 1 element
    def test_multiple_elements(self):
        # Test input - list with many values
        list = [2, 1, 3]

        # Initialize the manipulator with the test input
        list_manipulator = ListManipulator(list)
        
        # If the min method works properly, the output should be equal to 1 in this case
        self.assertEqual(list_manipulator.min(), 1)

    # Test the min method with an empty list
    def test_no_elements(self):
        # Test input - list with no values
        list = []
        list_manipulator = ListManipulator(list)

        # If the min method works properly, the output should be None for an empty list
        self.assertEqual(list_manipulator.min(), None)

class TestListManipulatorMax(unittest.TestCase):


class TestListManipulatorRemove(unittest.TestCase):


unittest.main()