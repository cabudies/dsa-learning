def merge(a1,a2,a):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if(a1[i]<a2[j]):
            a[k]=a1[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while i<len(a1):
        a[k]=a1[i]
        k=k+1
        i=i+1
    while j<len(a2):
        a[k]=a2[j]
        k=k+1
        j=j+1

def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid = len(arr)//2
    first_list = arr[:mid]
    second_list = arr[mid:]

    mergeSort(first_list)
    mergeSort(second_list)
    merge(first_list, second_list, arr)

# Main
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))

n = 6
arr = [2, 6, 8, 5, 4, 3]

mergeSort(arr)
print(*arr)
