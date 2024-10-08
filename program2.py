def romanToInt(s: str) -> int:
    """
    Convert a Roman numeral to an integer.
    
    :param s: Roman numeral string
    :return: Integer value
    """
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

# Test cases for the romanToInt function
def test_romanToInt():
    assert romanToInt("III") == 3, "Test case 1 failed"
    assert romanToInt("LVIII") == 58, "Test case 2 failed"
    assert romanToInt("MCMXCIV") == 1994, "Test case 3 failed"
    assert romanToInt("IV") == 4, "Test case 4 failed"
    assert romanToInt("IX") == 9, "Test case 5 failed"
    assert romanToInt("XL") == 40, "Test case 6 failed"
    assert romanToInt("XC") == 90, "Test case 7 failed"
    assert romanToInt("CD") == 400, "Test case 8 failed"
    assert romanToInt("CM") == 900, "Test case 9 failed"
    
    print("All test cases passed!")

# Run the test function
test_romanToInt()



