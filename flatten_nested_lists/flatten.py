def flatten(nested_list):
    """
    Flattens a nested list into a single list of integers.
    
    Args:
        nested_list: A list that may contain integers or other nested lists
        
    Returns:
        A flat list containing all integers in left-to-right order
    """
    if not nested_list:
        return []
    
    result = []
    stack = [nested_list]
    
    while stack:
        current = stack.pop()
        
        if isinstance(current, list):
            # Process list items in reverse order to maintain left-to-right order
            stack.extend(reversed(current))
        else:
            # Add integers to result
            result.append(current)
    
    return result