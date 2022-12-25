from sys import setrecursionlimit
setrecursionlimit(11000)


def stair_case(steps):
    if (steps == 0 ):
        return 1
    elif (steps < 0):
        return 0
 
    else:
        return stair_case(steps - 3) + stair_case(steps - 2) + stair_case(steps - 1)

# steps = int(input())
# steps = 4 # 7
steps = 5 # 13
result = stair_case(steps)
print(result)
