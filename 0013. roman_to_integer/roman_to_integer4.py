# memory O(1), runtime O(n)
def romanToInt(s):
    hash1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    hash2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

    res = 0
    i = 0

    while i < len(s):
        if i < len(s) - 1 and s[i:i+2] in hash2:
            res += hash2[s[i:i+2]]
            i += 2
        else:
            res += hash1[s[i]]
            i += 1
      
    return res

# print(romanToInt("III")) # 3
# print(romanToInt("LVIII")) # 58
print(romanToInt("MCMXCIV")) # 1994
# a= [0,1,2,3,4]
# print(a[0:1])