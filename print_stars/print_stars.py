# N = 3 number of symbols = N * 2 - 1 = 5
# __*__
# _***_
# *****
# _***_
# __*__

# N = 5 number of symbols = N * 2 -1 = 9
# ____*____
# ___***___
# __*****__
# _*******_
# *********
def print_stars(n):
  for i in range(1, n+1):
    n_spaces = n-i
    n_stars = i
    # print('_'*n_spaces,'*'*((n_stars-1)*2+1),'_'*n_spaces)
    print('_'*n_spaces,'*'*((n_stars-1)*2+1))

  for i in range(n-1, 0, -1):
    n_spaces = n-i
    n_stars = i
    # print('_'*n_spaces,'*'*((n_stars-1)*2+1),'_'*n_spaces)
    print('_'*n_spaces,'*'*((n_stars-1)*2+1))

print(print_stars(4))



def create_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
        
create_diamond(5)

n=4
i = 0
' ' * 3 + '*' * 1
i = 1
' ' * 2 + '*' * 3
i = 2
' ' * 1 + '*' * 5
i = 3
' ' * 0 + '*' * 7

# bottom triangle
i = 2
' ' * 1 + '*' * 5
i = 1
' ' * 2 + '*' * 3
i = 0
' ' * 3 + '*' * 1





