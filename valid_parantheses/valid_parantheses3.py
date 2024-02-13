def valid_parantheses(sequence, a):


  # Initialize a stack and a boolean variable `found` to `False`.
  stack = []
  found = False

  # Iterate through the input sequence.
  for char in sequence:
    # If the current character is an opening parenthesis, push it onto the stack.
    if char == '(':
      stack.append(char)

    # If the current character is a closing parenthesis.
    elif char == ')':
      # If the stack is empty, return `False`.
      if not stack:
        return False

      # Pop the topmost element from the stack.
      popped = stack.pop()
      # If the popped element is not the matching opening parenthesis, return `False`.
      if popped != '(':
        return False

    # If the current character is `a`.
    elif char == a:
      # Set `found` to `True`.
      found = True

  # If `found` is `False`, return `False`.
  if not found:
    return False

  # If the stack is not empty, return `False`.
  if stack:
    return False

  # Otherwise, return `True`.
  return True

print(valid_parantheses('(()))','a'))
print(valid_parantheses('(()))[]','a'))
print(valid_parantheses('(())[]','a'))
print(valid_parantheses('((})[]','a'))
print(valid_parantheses("{()}[]",'a'))
print(valid_parantheses('(())[]','a'))