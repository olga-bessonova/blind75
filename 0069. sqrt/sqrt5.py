def mySqrt(x):
    for n in range(x // 2 + 3):
        if n * n <= x and (n+1) * (n+1) > x:
            return n
print(mySqrt(4)) # 2
print(mySqrt(8)) # 2
print(mySqrt(1)) # 1
print(mySqrt(0)) # 0
# print(1//2)