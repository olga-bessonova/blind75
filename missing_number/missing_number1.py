from typing import List

def missing_number(arr: List[int]) -> int:
    n = len(arr) + 1  
    total_sum = n * (n + 1) // 2  
    actual_sum = sum(arr)  
    missing_number = total_sum - actual_sum  
    return missing_number

arr = [1, 2, 3, 5]
print(missing_number(arr))  # Output: 4

arr = [6, 7, 8, 9, 11, 10]
print(missing_number(arr))  # Output: 12
