def order(sentence):
    hash = {}
    
    num = '123456789'
    arr = sentence.split()
    
    for word in arr:
        for i, n in enumerate(word):
            if n in num:
                hash[int(n)] = word
    
    res = []
    
    for i in range(1, len(arr)+1):
        res.append(hash[i])
    
    return ' '.join(res)

print(order("is2 Thi1s T4est 3a")) # "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2")) # "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
           