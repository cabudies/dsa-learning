def firstIndex(arr, x, result_index):
    if len(arr) < 1 or result_index>=len(arr):
        return -1
    if arr[result_index] == x:
        return result_index
    result = firstIndex(arr, x, result_index+1)
    return result


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x, 0))