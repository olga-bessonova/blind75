import re

def parser(user_info):

    user_info_values = user_info.split("0")
    # user_info_values = [x for x in with_empty_strings if x != '']

    check_username = re.match(r'[A-Za-z_]+', user_info_values[0])
    check_firstname = re.match(r'[A-Za-z]+', user_info_values[1])
    check_lastname = re.match(r'[A-Za-z]+', user_info_values[2])
    check_id = re.match(r'[1-9]+', user_info_values[3])

    if not (check_username and check_firstname and check_lastname ):
        raise ValueError("Invalid user info")

    return {
        "username": check_username.group(),
        "firstname": check_firstname.group(),
        "lastname": check_lastname.group(),
        "id": check_id.group(),
    }

# print(parser('thatoneguy00Brad0Pitt0000156742'))
print(parser('will_s00Will0Smith0000911'))