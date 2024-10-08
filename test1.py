from program1 import isValid  # Importing the isValid function

def test_isValid():
    # Test case 1: Balanced parentheses
    assert isValid("()") == True, "Test case 1 failed"
    
    # Test case 2: Balanced mixed parentheses
    assert isValid("()[]{}") == True, "Test case 2 failed"
    
    # Test case 3: Nested balanced parentheses
    assert isValid("{[()]}") == True, "Test case 3 failed"
    
    # Test case 4: Unbalanced parentheses (closing without opening)
    assert isValid("(]") == False, "Test case 4 failed"
    
    # Test case 5: Unbalanced nested parentheses
    assert isValid("([)]") == False, "Test case 5 failed"
    
    # Test case 6: Empty string (valid case)
    assert isValid("") == True, "Test case 6 failed"
    
    # Test case 7: Single opening bracket (invalid case)
    assert isValid("(") == False, "Test case 7 failed"
    
    # Test case 8: Single closing bracket (invalid case)
    assert isValid(")") == False, "Test case 8 failed"
    
    print("All test cases passed!")

# Run the test function
test_isValid()
