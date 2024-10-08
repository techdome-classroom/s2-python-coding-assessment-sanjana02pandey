from program import romanToInt  # Ensure the file name is correct

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



