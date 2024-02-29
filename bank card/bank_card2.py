import re

def is_valid_credit_card(card_number):
    pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'

    if re.match(pattern, card_number):
        digits_only = ''.join(filter(str.isdigit, card_number))
        if any(digit * 4 in digits_only for digit in set(digits_only)):
            return False  
        else:
            return True   
    else:
        return False      

print(is_valid_credit_card('4-5678-9012-3456'))
print(is_valid_credit_card('5122-2368-7954 - 3214'))
print(is_valid_credit_card('44244x4424442444'))
print(is_valid_credit_card('4555362587961578'))
