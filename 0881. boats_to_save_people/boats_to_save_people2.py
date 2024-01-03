def numRescueBoats(people, limit):
  people.sort() # [3,3,4,5]

  boats = 0
  l, r = 0, len(people) - 1 # l,r = 0,3
  while l <= r: # 0 <= 1
      remain = limit - people[r] # remain = 5-3 = 2
      r -= 1 # 1
      boats += 1 # 2
      # while people[l] <= remain and l <= r: # this solution when there is no limit of people in a boat
      if people[l] <= remain and l <= r: # 3<=1 and True
          # remain -= people[l]
          l += 1 # l = 0
  return boats
# print(numRescueBoats(people = [1,2], limit = 3)) # 1
# print(numRescueBoats(people = [1,4], limit = 3)) # 1
# print(numRescueBoats(people = [3,5,3,4], limit = 5)) # 4
# print(numRescueBoats(people = [1,1,1,1,5], limit = 9)) # 1
print(numRescueBoats(people =[2, 2, 2, 6, 6, 7, 10, 10, 10, 11, 12, 13, 18, 22, 26, 33, 41, 47, 49, 50], limit = 50)) # 11
# a = [2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10]
# a.sort()
# print(a)
# [2, 2, 2, 6, 6, 7, 10, 10, 10, 11, 12, 13, 18, 22, 26, 33, 41, 47] 2
# [ 2, 2, 6, 6, 7, 10, 10, 10, 11, 12, 13, 18, 22, 26, 33, 41] 3
# [ 6, 6, 7, 10, 10, 10, 11, 12, 13, 18, 22, 26, 33] 4
# [ 7, 10, 10, 10, 11, 12, 13, 18, 22, 26] 5
# [  10, 10, 11, 12, 13, 18, 22] 6
# [  11, 12, 13, 18] 7
# [  13] 8
# [ ] 9
