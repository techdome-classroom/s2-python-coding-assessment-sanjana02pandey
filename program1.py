def isValid(s: str) -> bool:
    """
    Returns true if the input string is valid, false otherwise.
    """
    # Initialize an empty stack
    stack = []
    
    # Mapping of closing brackets to opening brackets
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    # Iterate through the input string
    for char in s:
        # If the current character is an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)
        # If the current character is a closing bracket, check if the stack is empty or the top of the stack does not match
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False
    
    # If the stack is not empty after iterating through the entire string, return false
    return not stack







    



  








    



  

