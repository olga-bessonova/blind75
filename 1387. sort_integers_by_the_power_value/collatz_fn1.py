# collatz_fn(n):
#.  3*n+1 if n is odd
#.  n / 2 if n is even

# collatz_sequence(5):  5 -> 16 -> 8 -> 4 -> 2 -> 1 # five hops
# collatz_hops(5) = 5 # Starting at 5, it took 5 hops to get to 1.
# 4 -> 2 -> 1
# highest_collatz_number(10) 


# You are given number n
# do this until n == 1: 
# #.  3*n+1 if n is odd
# #.  n / 2 if n is even

# steps = hops.
# For example, n = 5: 5 -> 16 -> 8 -> 4 -> 2 -> 1 # five hops
# For example, n = 4: 4 -> 2 -> 1 # two hops
# Now, the next part of the question is this. You are given a number N
# among numbers [2..N] find the one with the max amount of hops

import time
# do brutal force and then find more efficient solution   
###############------Brutal force solution------################################
start = time.time()
def highest_collatz_number(maximum):
  # highest_collatz_number(10) -> the biggest collatz_hops(x) for x in [2..10]
  arr = list(collatz_hops(n) for n in range(2, maximum+1))
  print(max(arr))
  return arr.index(max(arr)) + 2
end = time.time()
print("execution time 1 = ", end - start)

###############------more optimal solution------################################
# start = time.time()
# def highest_collatz_number(maximum):
#   hash = {}
#   for i in range(2, maximum + 1):
#     if i/2 in hash:
#       hash[i] =  hash[i/2] + 1
#     else:   
#       hash[i] = collatz_hops(i)
    
#   return max(hash.values())
# end = time.time()

# print("execution time 2 = ", end - start)
  
  
def collatz_hops(n):  
  hops = 0
  while n > 1:
    if n % 2 == 0:
      n = n / 2
    else:
      n = 3*n+1
    hops += 1    
  return hops
# hash = {'A': 1, 'b':999}

# print(hash['c'])
print(highest_collatz_number(10)) # 9 -> 28 -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1


  