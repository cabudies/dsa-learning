from sys import setrecursionlimit
setrecursionlimit(20)

def string_to_integer(string, number):
    if len(string) == 0:
        return number
    if int(string[0]) != 0:
        number = number*10 + int(string[0])
    return string_to_integer(string[1:], number)

# string = "00001231" # 1231
# string = "12567" # 12567
string = input()
result = string_to_integer(string=string, number=0)
print(result)

