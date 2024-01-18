from collections import defaultdict
def groupThePeople(groupSizes):
        dic = defaultdict(list)
        res = []
        for ind, size in enumerate(groupSizes):
            if len(dic[size]) == size:
                res.append(dic[size])
                dic.pop(size)
            dic[size].append(ind)

        for key in dic:
            res.append(dic[key])
    
        return res
print(groupThePeople([3,3,3,3,3,1,3]))