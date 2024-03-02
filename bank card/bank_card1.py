import re

def is_valid_credit_card(card_number):
    # Define the regex pattern
    pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'

    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        # Check for consecutive repeated digits
        digits_only = ''.join(filter(str.isdigit, card_number))
        if any(digit * 4 in digits_only for digit in set(digits_only)):
            return False  # More than three consecutive repeated digits found
        else:
            return True   # Valid credit card number
    else:
        return False      # Pattern not matched

# Example usage:
card_number = "4-5678-9012-3456"
print(is_valid_credit_card('4-5678-9012-3456'))
print(is_valid_credit_card('5122-2368-7954 - 3214'))
print(is_valid_credit_card('44244x4424442444'))
print(is_valid_credit_card('4555362587961578'))
