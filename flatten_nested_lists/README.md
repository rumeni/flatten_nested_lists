# Flatten Nested Lists

A Python solution that flattens nested lists of integers into a single list while preserving left-to-right order.

## Problem Description

Given a list containing integers or nested lists (which themselves may contain integers or other lists to arbitrary depth), return a flat list of all integers in their original left-to-right order.

**Constraints:**
- Supports arbitrary nesting depth
- Integer values: -10^9 ≤ x ≤ 10^9
- List length ≤ 10^4 per level
- Total integers ≤ 10^5

## Examples

```python
flatten([[123], [[1],[2,[3,4]]]])  # [123, 1, 2, 3, 4]
flatten([1,[2,[3,[4,[5]]]]])       # [1, 2, 3, 4, 5]  
flatten([])                        # []
flatten([[[[42]]]])                # [42]
flatten([1, [2, 3], [[4]], 5])    # [1, 2, 3, 4, 5]
```

## Usage

```python
from flatten import flatten

# Basic usage
result = flatten([1, [2, [3, 4]], 5])
print(result)  # [1, 2, 3, 4, 5]

# Handle empty lists
result = flatten([[], [1, []], [2]])
print(result)  # [1, 2]

# Work with negative numbers
result = flatten([-1, [0, [-2, [3]]]])
print(result)  # [-1, 0, -2, 3]
```

## Testing

Run the comprehensive test suite:

```bash
python -m unittest test_flatten.py -v
```

The test suite includes:
- All requirement examples
- Edge cases (empty lists, single elements)
- Boundary values and constraints
- Complex nested structures

## Implementation Details

- **Algorithm**: Iterative approach using a stack
- **Time Complexity**: O(n) where n is total number of elements
- **Space Complexity**: O(d) where d is maximum nesting depth
- **Benefits**: Handles arbitrary depth without recursion limits

## Files

- `flatten.py` - Main implementation
- `test_flatten.py` - Comprehensive test suite (10 tests)
- `README.md` - This documentation