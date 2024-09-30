def lengthOfLastWord(s):
    # Initialize pointers and length counter
    i, length = len(s) - 1, 0

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # Count characters in the last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length

# Test cases
print(lengthOfLastWord("Hello World"))  # Output: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
