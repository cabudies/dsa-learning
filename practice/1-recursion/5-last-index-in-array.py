def firstIndex(arr, x, result_index):
    if result_index == len(arr):
        return -1
    if arr[result_index] == x:
        return result_index
    result = firstIndex(arr[:-1], x, result_index-1)
    return result


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
# arr = [9, 8, 10, 8]
# x = 9
# x = 8
print(firstIndex(arr, x, len(arr)-1))