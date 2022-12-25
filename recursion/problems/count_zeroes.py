from sys import setrecursionlimit
setrecursionlimit(20)

def number_of_zeroes(number, zeroes_count):
    if number == 0:
        return zeroes_count
    if number%10 == 0:
        zeroes_count = zeroes_count + 1
    return number_of_zeroes(int(number/10), zeroes_count)
    

# number = "00010204" # 2
# number = "708000" # 4
number = input()
int_number = int(number)
result = number_of_zeroes(int_number, 0)
print(result)
