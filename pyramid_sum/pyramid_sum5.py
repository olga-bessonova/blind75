def pyramid_sum(base):
    if len(base) == 1:
        return [base]
    
    next_level = [base[i] + base[i+1] for i in range(len(base) - 1)]
    
    return pyramid_sum(next_level) + [base]

print(pyramid_sum([1, 4, 6]))  # Output: [[15], [5, 10], [1, 4, 6]]
print(pyramid_sum([3, 7, 2, 11]))  # Output: [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]
