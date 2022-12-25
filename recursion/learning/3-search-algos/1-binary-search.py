def binarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]>x:
        return binarySearch(a,x,si,mid-1)
    else:
        return binarySearch(a,x,mid+1,ei)

arr = [1,3,5,7,9,11,13,15,16,17] # condition - list should be sorted always
x = 3
# x = 2
# x = 13
start_index = 0
end_index = len(arr)

print(binarySearch(arr, x, start_index, end_index))
