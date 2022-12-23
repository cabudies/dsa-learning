from sys import setrecursionlimit
setrecursionlimit(11000)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2) + fib(n-3)

def stair_case(steps):
    return fib(steps+1)

# value = input()
steps = 4 # 7
result = stair_case(steps)
print(result)
