# The fibonacci sequence is a sequence of numbers whose first and second elements are 1. 
# To generate further elements of the sequence we take the sum of the previous two elements. 
# For example the first 6 fibonacci numbers are 1, 1, 2, 3, 5, 8. 
# Write a function fibonacci that takes in a number length and 
# returns the fibonacci sequence up to the given length.

def fibonacci(length):
    # res = []
    if length == 0:
        return []
    elif length == 1:
        # res = [1]
        return [1]
    elif length == 2:
        return [1,1]
    else:
        res = fibonacci(length-1)
        res.append(prev[-1] + prev[-2])
        return res

print(fibonacci(0)) # []
print(fibonacci(1)) # [1]
print(fibonacci(6))  # [1, 1, 2, 3, 5, 8]
print(fibonacci(8))  # [1, 1, 2, 3, 5, 8, 13, 21]