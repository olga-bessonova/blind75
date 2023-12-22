def collision(asteroids):
  sub_asteroids = [asteroids[0]]
  active_asteroid = []

  for i in range(1, len(asteroids)):
    if (sub_asteroids[-1] * asteroids[i] > 0) or (sub_asteroids[-1] < 0 and asteroids[i] > 0):
      sub_asteroids.append(asteroids[i])
    else:
      active_asteroid.append(asteroids[i])
      while len(active_asteroid) > 0:
        print("i: ", i)
        print("sub_asteroids:", sub_asteroids)
        if (abs(sub_asteroids[-1]) == abs(active_asteroid[-1]) and 
                sub_asteroids[-1] * active_asteroid[-1] < 0):
          sub_asteroids.pop()
          active_asteroid.pop()

        elif abs(sub_asteroids[-1]) < abs(active_asteroid[-1]):
          while ((abs(sub_asteroids[-1]) < abs(active_asteroid[-1])) and 
                 sub_asteroids[-1] * active_asteroid[-1] < 1):
            # print("2nd while sub_asteroids: ", sub_asteroids)
            sub_asteroids.pop()
            if (abs(sub_asteroids[-1]) == abs(active_asteroid[-1]) and 
                sub_asteroids[-1] * active_asteroid[-1] < 0):
              print("if 2nd while sub_asteroids: ", sub_asteroids)
              print("if 2nd while active_asteroid: ", active_asteroid)
              sub_asteroids.pop()
              active_asteroid.pop()
              print("if 2nd while sub_asteroids: ", sub_asteroids)
              print("if 2nd while active_asteroid: ", active_asteroid)
              break
            # print("2nd while sub_asteroids: ", sub_asteroids)
            # print("2nd while active_asteroid: ", active_asteroid)
            else:
              sub_asteroids.append(asteroids[i])
          if (len(sub_asteroids) == 1) and len(active_asteroid) > 0:
            active_asteroid.pop()
            break

        else:
          active_asteroid.pop()
          print(" else statement active_asteroid:", active_asteroid)
          continue
  return sub_asteroids

# print(collision([5,10,-5])) # [5,10]
# print(collision([8,-8])) # []
# print(collision([10,2,-5])) # [10]
# print(collision([1,2,3,-3,4,-2,-1])) # [1,2,4]
# print(collision([-2,-1,1,2])) # [-2,-1,1,2]
# print(collision([-2,-2,1,-2])) # [-2,-2,-2]
# print(collision([-2,1,1,-2])) # [-2,-2]
print(collision([10,2,-5])) # [10]





