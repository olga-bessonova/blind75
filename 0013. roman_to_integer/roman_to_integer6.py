def roman_to_int(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    special_values = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    result = 0
    i = 0
    length = len(s)

    while i < length:
        if i < length - 1 and s[i:i+2] in special_values:
            result += special_values[s[i:i+2]]
            i += 2
        else:
            result += roman_values[s[i]]
            i += 1

    return result

print(roman_to_int("MCMXCIV"))  # 1994
