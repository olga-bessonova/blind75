def palindrome_check(string):
    """
    Checks if a given string is a palindrome or can be rearranged into a palindrome by permutation of letters.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is a palindrome or can be rearranged into a palindrome, False otherwise.
    """

    # Convert the string to lowercase and remove all spaces.
    string = string.lower().replace(" ", "")

    # Convert the string to a set to remove duplicate characters.
    char_set = set(string)

    # Check if the length of the set is even.
    if len(char_set) % 2 == 0:
        return True

    # Check if there is only one character that appears an odd number of times.
    odd_count = 0
    for char in char_set:
        if string.count(char) % 2 == 1:
            odd_count += 1

    return odd_count == 1

print(palindrome_check("hello"))
print(palindrome_check("ivicc"))
print(palindrome_check("civic"))