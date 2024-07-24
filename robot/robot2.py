import numpy as np
def robot(moves):
  # R (Right), L (Left), U (Up) and D (down)
  position = [0,0]
  hash = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1]}
  for move in moves:
    # update x axis:
    position[0] += hash[move][0]
    # update y axis:
    position[1] += hash[move][1]
    position += hash[move]
    # position = np.add(position, hash[move])
    # print("i, position: ", move, position)

  
  return position == [0,0]

print(robot('UD'))
# print(robot('LL'))
