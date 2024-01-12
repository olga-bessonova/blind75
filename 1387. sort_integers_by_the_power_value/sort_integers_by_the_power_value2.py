def getKth(lo, hi, k):
  res = []
  for num in range(lo, hi+1):
    pow = 0
    n = num
    while n > 1:
      if n % 2 == 0:
        n /= 2
      else:
        n = 3*n + 1
      pow += 1
    res.append([num, pow])
  res.sort(key=lambda x: x[1])
  return res[k-1][0]



print(getKth(12,15,2))


# my_dict = {'banana': 3, 'apple': 1, 'orange': 2}
# sorted_dict_values = list(sorted(my_dict.items(), key=lambda item: item[0]))
# print(sorted_dict_values)