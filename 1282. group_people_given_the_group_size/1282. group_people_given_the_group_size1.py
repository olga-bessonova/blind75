def groupThePeople(groupSizes):
    hash = {}
    for i in range(len(groupSizes)):
        if groupSizes[i] in hash:
            hash[groupSizes[i]].append(i)
        else:
            hash[groupSizes[i]] = [i]

    res = []

    for key in hash.keys():
        i = len(hash[key]) // key
        print(i)
        while i > 0:
            # print
            # print(hash[key][i*key-key:i*key])
            res.append(hash[key][i*key-key:i*key])
            i -= 1
    return res  
arr = [3,3,3,3,3,1,3]
# hash = {3: [0, 1, 2, 3, 4, 6], 1: [5]}
# print(hash[3][0:3])
# print(hash[3][3:6])
print(groupThePeople(arr))
# abc = [0,1,2,3,4,5,6]
# print(abc[])
# print(4/2)
# print(4//2)