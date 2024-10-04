def isValid(s: str) -> bool:
    stack = []
    
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_parentheses:
            top_element = stack.pop() if stack else '#'
            if matching_parentheses[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack
s = "()[]{}"
print(isValid(s))  # Output: True

s = "([)]"
print(isValid(s))  # Output: False

s = "{[]}"
print(isValid(s))  # Output: True
