def fibs(num):
    # If num < 0 return num because the Fibonacci sequence is not defined for negative numbers:
    if num < 0:
        return None
    elif num == 0:
        return []
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        # Use recursion to generate the previous sequences:
        arr = fibs(num - 1)
        arr.append(arr[-1] + arr[-2])
        return arr

# Example to execute this function:
print(fibs(5)) # output [1, 1, 2, 3, 5]
print(fibs(10)) # output [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(fibs(-1)) # output None