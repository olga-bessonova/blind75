def strStr(haystack, needle):

    for i in range(0, len(haystack) - len(needle) + 1):
        if needle == haystack[i:i+len(needle)]:
            return i
    return -1

print(strStr("sadbutsad", "sad")) # 0
print(strStr("leetcode", "leeto")) # -1

