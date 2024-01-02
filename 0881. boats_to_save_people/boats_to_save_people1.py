# runtime O (nxn), memory O (n)
def numRescueBoats(people, limit):
  boats = 0
  limit_left = 3
  i=0
  while len(people) > 0: 
      if people[i] < 0 or people[i] > limit:
          return None
      elif people[i] == limit:
          boats += 1 
          people.pop(i) 
      else:
          limit_left -= people[i] 
          people_in_the_boat = []
          while limit_left > 0:
              
              # print("i, people, people_in_the_boat, limit_left: ", i, people, people_in_the_boat, limit_left)
              if people[i+1]:
                  for j in range(i+1, len(people)):
                      # print("j people[j] <= limit_left: ", j, people[j], limit_left)
                      if people[j] <= limit_left: 
                          limit_left -= people[j] 
                          people_in_the_boat.append(j) 
                      if j == len(people)-1:
                          break
          boats += 1 
          # print("boats = ", boats)
          people_in_the_boat.append(i)
          # print("people_in_the_boat = ", sorted(people_in_the_boat, reverse = True))
          for index in sorted(people_in_the_boat, reverse = True):
              # print('people = ', people)
              people.pop(index) 
              # print('people = ', people)

  return boats

print(numRescueBoats(people = [1,2], limit = 3)) 
print(numRescueBoats(people = [3,2,2,1], limit = 3)) 