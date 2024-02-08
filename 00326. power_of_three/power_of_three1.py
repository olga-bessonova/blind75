def isPowerOfThree(n):
        if n <= 0:
            return False
        elif n == 1:
            return True

        while n >= 1:  
            if n % 3 == 0:
                # print("n: ",n)
                # print("n/3: ",n/3)
                n /= 3
                if n == 1:
                    return True
                # print("new n:", n)
            else:
                return False
            
print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(-1))