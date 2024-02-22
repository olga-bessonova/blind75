def decimal_to_binary(n):
  """
  This function converts a decimal number to a binary number.

  Args:
    n: The decimal number to convert.

  Returns:
    The binary representation of the decimal number.
  """

  if n == 0:
    return "0"

  binary_digits = []

  while n > 0:
    remainder = n % 2
    n //= 2
    binary_digits.append(str(remainder))

  return "".join(reversed(binary_digits))


# Example usage:
print(decimal_to_binary(10))  # Output: 1010
print(decimal_to_binary(1))  # Output: 1
print(decimal_to_binary(20))  # Output: 10100
print(decimal_to_binary(0))  # Output: 0