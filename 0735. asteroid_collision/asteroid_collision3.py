# memory O(n), runtime O(1)
def collision(asteroids):
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if a + stack[-1] == 0:
                stack.pop()
                a = 0
            elif abs(stack[-1]) > abs(a):
                a = 0
            else:
                stack.pop()
        if a:
            stack.append(a)
    return stack
print(collision([5,10,-5])) # [5,10]
print(collision([8,-8])) # []
print(collision([10,2,-5])) # [10]
print(collision([1,2,3,-3,4,-2,-1])) # [1,2,4]
print(collision([-2,-1,1,2])) # [-2,-1,1,2]
print(collision([-2,-2,1,-2])) # [-2,-2,-2]
print(collision([-2,1,1,-2])) # [-2,-2]
print(collision([5,10,-5])) # [5,10]


