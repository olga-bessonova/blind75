# runtime O(n), memory O(1)
def lengthOfLastWord(s):
    i, length = len(s) - 1, 0

    while s[i] == ' ':
        i -= 1
    # print("III: ",i)
    for j in reversed(range(0,i+1)):
        # print("j: ", j)
        if s[j] == ' ':
            # print('break')
            break
        else:
            length += 1
        # print("i: ", i)
        # print("length: ", length)
    # print("length final: ", length)
    return length


print(lengthOfLastWord("Hello World")) # 5
print(lengthOfLastWord("   fly me   to   the moon  ")) # 4