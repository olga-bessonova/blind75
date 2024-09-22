def length_of_longest_substring(s: str) -> int:
    max_substring_length = 0

    for i in range(len(s)):
        substring = ''
        for j in range(i, len(s)):
            if s[j] not in substring:
                substring += s[j]
                max_substring_length = max(max_substring_length, len(substring))
            else:
                break

    return max_substring_length

print(length_of_longest_substring(' '))
# print(length_of_longest_substring('abca'))
