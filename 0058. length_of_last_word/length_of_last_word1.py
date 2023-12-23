def lengthOfLastWord(s):
    arr = s.split(' ')
    filtered_arr = [el for el in arr if el != '']
    return len(filtered_arr[-1])


print(lengthOfLastWord("Hello World")) # 5
print(lengthOfLastWord("   fly me   to   the moon  ")) # 4