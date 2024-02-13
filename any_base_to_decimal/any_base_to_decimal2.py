def converter(number, base):
  """Converts a number from any base system to a decimal numeral system.

  Args:
    number: The number to be converted.
    base: The base of the number.

  Returns:
    The decimal equivalent of the given number.
  """

  # Check if the number is negative.
  # if number < 0:
    # return "Please provide a non-negative number"

  # Check if the base is between 2 and 36.
  if base < 2 or base > 36:
    return "Please provide a number in a base system between 2 and 36"

  # Convert the number to a string.
  number_str = str(number)

  # Initialize the decimal equivalent.
  decimal_equivalent = 0

  # Iterate over each digit of the number.
  for i, digit in enumerate(number_str[::-1]):
    # Convert the digit to an integer.
    digit_int = int(digit,base)

    # Multiply the digit by its corresponding base value raised to the power of its position.
    product = digit_int * (base ** i)

    # Add the product to the decimal equivalent.
    decimal_equivalent += product

  # Return the decimal equivalent.
  return decimal_equivalent


# Test the converter function.
print(converter(123, 10))  # 123
print(converter(10101, 2))  # 21
print(converter('11A', 16))  # 532
