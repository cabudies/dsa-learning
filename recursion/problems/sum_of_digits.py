from sys import setrecursionlimit
setrecursionlimit(1100)

def digits_sum(value):
    if value == 0:
        return 0    
    small_value = value % 10
    return small_value + digits_sum(int(value/10))

# value = 12345
value = int(input())
result = digits_sum(value)
print(result)




