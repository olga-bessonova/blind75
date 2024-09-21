def same_char_collapse(s):
    arr = list(s)
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            arr.pop(i+1)
            arr.pop(i)
            i = 0  
        else:
            i += 1  
    return ''.join(arr)

print(same_char_collapse("zzzxaaxy"))  # Output: "zy"
print(same_char_collapse("uqrssrqvtt"))  # Output: "uv"
