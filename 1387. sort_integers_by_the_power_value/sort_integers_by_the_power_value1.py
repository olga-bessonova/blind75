def getKth(lo, hi, k):
    hash = {}
    for i in range(lo, hi+1):
        power = 0
        n = i
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            power += 1
        hash[i] = power
    sorted_hash = sorted(hash.items(), key=lambda x: x[1])
    return sorted_hash[k-1][0]
      
print(getKth(12,15,2))
        

    




