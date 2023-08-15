def countSubstrings(s):
    resArray = []

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            resArray.append(s[l:r+1])
            l -= 1
            r += 1
        
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            resArray.append(s[l:r+1])
            l -= 1
            r += 1
    print(resArray)
    return len(resArray)

print(countSubstrings('abc'))