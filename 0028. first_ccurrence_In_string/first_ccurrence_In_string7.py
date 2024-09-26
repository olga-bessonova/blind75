def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    needle_len = len(needle)

    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i

    return -1

# Test cases
print(str_str("sadbutsad", "sad"))  # 0
print(str_str("leetcode", "leeto"))  # -1
