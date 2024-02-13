def valid_parantheses(sequence, a):
  """
  Checks if parentheses are well-formatted and the letter 'a' is enclosed by parentheses.

  Args:
    sequence: A sequence of parentheses.
    a: A letter that may appear in the sequence.

  Returns:
    True if parentheses are well-formatted and 'a' is enclosed by parentheses, False otherwise.
  """

  stack = []

  for char in sequence:
    if char in '({[':  # Check if it's an opening parenthesis
      stack.append(char)

    elif char in ')}]':  # Check if it's a closing parenthesis
      if not stack or stack.pop() != {')': '(', '}': '{', ']': '['}[char]:
        return False

    elif char == a:  # Check if it's the letter 'a'
      if not stack or stack[-1] != '(':
        return False

  return not stack  # Check if the stack is empty, indicating well-formatted parentheses
print(valid_parantheses('(()))','a'))
print(valid_parantheses('(()))[]','a'))
print(valid_parantheses('(())[]','a'))
print(valid_parantheses('((})[]','a'))
print(valid_parantheses("{()}[]",'a'))
print(valid_parantheses('(())[]','a'))