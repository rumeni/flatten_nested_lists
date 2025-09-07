"""
Test suite for flatten function.
"""

import unittest



from flatten import flatten


class TestFlatten(unittest.TestCase):
    """Essential tests for the flatten function."""
    
    def test_requirement_examples(self):
        """Test all examples from the problem statement."""
        # Example 1
        input_data = [[123], [[1],[2,[3,4]]]]
        expected = [123, 1, 2, 3, 4]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Example 1 failed: expected {expected}, got {actual}")
        
        # Example 2
        input_data = [1,[2,[3,[4,[5]]]]]
        expected = [1, 2, 3, 4, 5]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Example 2 failed: expected {expected}, got {actual}")
        
        # Example 3
        input_data = []
        expected = []
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Example 3 failed: expected {expected}, got {actual}")
        
        # Example 4
        input_data = [[[[42]]]]
        expected = [42]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Example 4 failed: expected {expected}, got {actual}")
    
    def test_flat_list(self):
        """Test with already flat list."""
        input_data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Flat list failed: expected {expected}, got {actual}")
    
    def test_mixed_nesting(self):
        """Test with mixed nesting levels."""
        input_data = [1, [2, 3], [[4]], [[[5]]]]
        expected = [1, 2, 3, 4, 5]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Mixed nesting failed: expected {expected}, got {actual}")
    
    def test_negative_and_zero(self):
        """Test with negative numbers and zero."""
        input_data = [-1, [0, [-2, [3]]]]
        expected = [-1, 0, -2, 3]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Negative/zero test failed: expected {expected}, got {actual}")
    
    def test_empty_nested_lists(self):
        """Test with empty lists at various levels."""
        input_data = [[], [1, []], [2, [[], 3]]]
        expected = [1, 2, 3]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Empty nested lists failed: expected {expected}, got {actual}")
    
    def test_deep_nesting(self):
        """Test with deep nesting (arbitrary depth)."""
        # Create [1, [2, [3, [4, [5]]]]]
        nested = [5]
        for i in range(4, 0, -1):
            nested = [i, nested]
        
        expected = [1, 2, 3, 4, 5]
        actual = flatten(nested)
        self.assertEqual(actual, expected, f"Deep nesting failed: expected {expected}, got {actual}")

    def test_single_element(self):
        """Test with single integer in a list."""
        input_data = 42
        expected = [42]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Single element failed: expected {expected}, got {actual}")

    def test_large_numbers(self):
        """Test with boundary values from constraints."""
        input_data = [1000000000, [-1000000000, [0]]]
        expected = [1000000000, -1000000000, 0]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Large numbers failed: expected {expected}, got {actual}")

    def test_multiple_empty_lists(self):
        """Test with multiple consecutive empty lists."""
        input_data = [[], [], [1], [], [2, []], []]
        expected = [1, 2]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Multiple empty lists failed: expected {expected}, got {actual}")

    def test_complex_structure(self):
        """Test with complex mixed structure."""
        input_data = [1, [2, [3]], [4, 5], [[6, [7]], 8], [[[9]]], 10]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = flatten(input_data)
        self.assertEqual(actual, expected, f"Complex structure failed: expected {expected}, got {actual}")


if __name__ == "__main__":
    unittest.main(verbosity=2)