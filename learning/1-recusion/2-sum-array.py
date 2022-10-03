def sumArray(arr):
    # Please add your code here
    if len(arr) < 1:
        return 0
    result = arr[0] + sumArray(arr[1:])
    return result

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))