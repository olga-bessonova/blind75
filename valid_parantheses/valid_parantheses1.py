def isValid(test_str):  
    par_dict = {'(':')','{':'}','[':']'}
    stack = []
    for char in test_str:
        if char in par_dict.keys(): 
            stack.append(char)
        elif char in par_dict.values():
          if stack == []:
              return False
          open_brac = stack.pop()
          if char != par_dict[open_brac]:
            return False
    return stack == []

print(isValid('(())'))
print(isValid('((a))'))
print(isValid('((a)))'))
print(isValid('((a)))[]'))
print(isValid('((a))[]'))
print(isValid('(())[]'))
print(isValid('(()a)[]'))