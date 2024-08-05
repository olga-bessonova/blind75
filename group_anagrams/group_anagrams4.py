def groupAnagrams(str):
    res = defaultdict(list)
    print(res)

    for s in str:
        count = [0]*26

        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return res.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])