from sys import setrecursionlimit
setrecursionlimit(11000)

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2) + fib(n-3)

def stair_case(steps):
    if (steps == 0 ):
        return 1
    elif (steps < 0):
        return 0
 
    else:
        return stair_case(steps - 3) + stair_case(steps - 2) + stair_case(steps - 1)

# value = input()
# steps = 4 # 7
steps = 5 # 13
result = stair_case(steps)
print(result)
