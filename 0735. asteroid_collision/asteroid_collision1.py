def collision(asteroids):
        
      

def collision(asteroids):
  sub_asteroids = [asteroids[0]]
	active_asteroid = []
	
  for i in range(1,len(asteroids)):
	  if (sub_asteroids[0] > 0 and asteroids[i] > 0) or (sub_asteroids[0] < 0  and asteroids[i] < 0):
			sub_asteroids.append(asteroids[i])
		else:
			active_asteroid.append(asteroids[i])
			while len(active_asteroid) > 0:
        if abs(sub_asteroids[-1]) == abs(asteroids[i]):
          sub_asteroids.pop()
          active_asteroid.pop()

        elif abs(sub_asteroids[-1]) < abs(asteroids[i]):
          sub_asteroids.pop()
          sub_asteroids.append(asteroids[i])
          if len(sub_asteroids) == 1:
            active_asteroid.pop()
            break

        else:
          active_asteroid.pop()
          continue
  return sub_asteroids

