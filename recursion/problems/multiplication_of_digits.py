from sys import setrecursionlimit
setrecursionlimit(1100)

def digits_multiplication(base_value, limit_value):
    if limit_value == 0:
        return 0
    small_answer = digits_multiplication(base_value, limit_value-1)
    return base_value + small_answer

first_value = int(input())
limit_value = int(input())

result = digits_multiplication(first_value, limit_value)
print(result)

