# Isaac Krementsov
# 11/25/19
# List Manipulator Test - Test cases for the ListManipulator class methods
# The Github repo for this code is at https://github.com/isaackrementsov-edu/list-manipulator-testing

# Get the unittest package and ListManipulator class from ListManipulator.py
import unittest
from ListManipulator import ListManipulator


# Test the ListManipulator's min method with a variety of inputs
# - The min method finds the min value of a list, returning None if the list is empty
# Test Case classes extend the unittest.TestCase superclass
class TestListManipulatorMin(unittest.TestCase):
    # Test the min method with a list containing more than 1 element
    def test_multiple_elements(self):
        # Test input - list with many values
        list = [2, 1, 3]

        # Initialize the manipulator with the test input by passing it into the constructor
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


# Test the ListManipulator's max method with a variety of inputs
# - The max method should return the max value in a list, or None if the list is empty
class TestListManipulatorMax(unittest.TestCase):
    # Test the max method with a list containing more than 1 element
    def test_multiple_elements(self):
        # Test input - list with many values
        list = [2, 1, 3]
        list_manipulator = ListManipulator(list)

        # If the max method works properly, the output should be equal to 3 in this case
        self.assertEqual(list_manipulator.max(), 3)

    # Test the max method with an empty list
    def test_no_elements(self):
        # Test input - list with no values
        list = []
        list_manipulator = ListManipulator(list)

        # If the max method works properly, the output should be None for an empty list
        self.assertEqual(list_manipulator.max(), None)


# Test the ListManipulator's remove method with a variety of inputs
# - The remove method should remove all occurrences of a given value in a list
class TestListManipulatorRemove(unittest.TestCase):
    def test_one_occurrence(self):
        # Test input - list with one occurrence of the value to remove
        list = [1, 2, 3]
        list_manipulator = ListManipulator(list)

        # Remove 1 from the list
        list_manipulator.remove(1)

        # If the remove method works properly, the list should now be [2, 3]
        self.assertEqual(list_manipulator.list, [2, 3])

    def test_multiple_occurrences(self):
        # Test input - list with multiple occurrences of the value to remove
        list = [1, 2, 3, 1]
        list_manipulator = ListManipulator(list)

        # Remove all 1s from the list
        list_manipulator.remove(1)

        # If the remove method works properly, the list should now be [2, 3]
        self.assertEqual(list_manipulator.list, [2, 3])


# Run the unittest main method, which calls all of the Test Cases
unittest.main()