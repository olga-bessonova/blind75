def decimal_to_ternary(num):
     # Check if the input is negative
    if num < 0:
        return "Input must be a positive number or 0"

    # Initialize an empty string to store the ternary representation
    ternary = ""

    # Repeatedly divide the decimal number by 3 and get the remainder
    while num > 0:
        remainder = num % 3
        ternary = str(remainder) + ternary
        num //= 3

    # If the input number is 0, return "0"
    if not ternary:
        return "0"

    return ternary
print(decimal_to_ternary(25))
print(decimal_to_ternary(10))
print(decimal_to_ternary(-1))