def collision(asteroids):
  sub_asteroids = [asteroids[0]]
  active_asteroid = []

  for i in range(1, len(asteroids)):
      flag = True
      active_asteroid.append(asteroids[i])
      while flag:
        flag = False
        if len(sub_asteroids) == 0:
          sub_asteroids.append(active_asteroid[-1])
          active_asteroid.pop()
          continue

        if (sub_asteroids[-1] * asteroids[i] > 0) or (sub_asteroids[-1] < 0 and asteroids[i] > 0):
          sub_asteroids.append(asteroids[i])
          active_asteroid.pop()
        elif abs(sub_asteroids[-1]) == abs(active_asteroid[-1]) and sub_asteroids[-1] < 0 and active_asteroid[-1] > 0:
          sub_asteroids.append(active_asteroid[-1])
          active_asteroid.pop()
        elif abs(sub_asteroids[-1]) == abs(active_asteroid[-1]) and sub_asteroids[-1] > 0 and active_asteroid[-1] < 0:
          sub_asteroids.pop()
          active_asteroid.pop()
        elif abs(sub_asteroids[-1]) == abs(active_asteroid[-1]) and sub_asteroids[-1] * active_asteroid[-1] > 0:
          sub_asteroids.append(asteroids[i])
          active_asteroid.pop()
        elif abs(sub_asteroids[-1]) > abs(active_asteroid[-1]):
          active_asteroid.pop()
        else:
          sub_asteroids.pop()
          if len(sub_asteroids) == 0:
            sub_asteroids.append(asteroids[i])
            active_asteroid.pop()
          else:
            flag = True
      if len(active_asteroid) > 0:
        sub_asteroids.append(active_asteroid[-1])
  return sub_asteroids

print(collision([5,10,-5])) # [5,10]
print(collision([8,-8])) # []
print(collision([10,2,-5])) # [10]
print(collision([1,2,3,-3,4,-2,-1])) # [1,2,4]
print(collision([-2,-1,1,2])) # [-2,-1,1,2]
print(collision([-2,-2,1,-2])) # [-2,-2,-2]
print(collision([1,-1,-2,-2])) # [-2,-2]
print(collision([10,2,-5])) # [10]





