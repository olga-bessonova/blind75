import re

def decoder(encoded_string):
    """
    Decodes a string containing encoded user information.

    Args:
    encoded_string: A string containing username, first name, last name, and id separated by zeros.

    Returns:
    A dictionary containing the decoded user information.
    """

    # Split the string by zeros to obtain the individual fields.
    fields_with_empty_strings = encoded_string.split("0")
    fields = [x for x in fields_with_empty_strings if x != '']

    # Validate and extract the fields using regular expressions.
    match_username = re.match(r'[A-Za-z_]+', fields[0])
    match_firstname = re.match(r'[A-Za-z]+', fields[1])
    match_lastname = re.match(r'[A-Za-z]+', fields[2])
    match_id = re.match(r'[1-9]+', fields[3])

    # Raise an error if any field is invalid.
    if not (match_username and match_firstname and match_lastname and match_id):
        raise ValueError("Invalid encoded string.")

    # Return a dictionary containing the decoded user information.
    return {
        "username": match_username.group(),
        "firstname": match_firstname.group(),
        "lastname": match_lastname.group(),
        "id": int(match_id.group()),
    }

print(decoder('thatoneguy00Brad0Pitt0000156742'))
print(decoder('luv_u00U0Smith0000898'))