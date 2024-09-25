def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""

    for i in range(len(strs[0])):
        current_char = strs[0][i]
        for s in strs:
            if i >= len(s) or s[i] != current_char:
                return prefix
        prefix += current_char

    return prefix

# Test cases
# print(longest_common_prefix(["abca","aba","aaab"])) # 'a'
# print(longest_common_prefix(["flower","flower","flower","flower"])) # 'flower'
print(longest_common_prefix(["flower", "flow", "flight"]))  # 'fl'
