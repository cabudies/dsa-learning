from sys import setrecursionlimit
setrecursionlimit(20)


def pair_star(original_string, new_string):
    if len(new_string)>0:
        if new_string[-1] == original_string[0]:
            new_string = new_string + "*"
    new_string = new_string + original_string[0] 
    if len(original_string)==1:
        return new_string
    
    return pair_star(original_string[1:], new_string)

# value = "hello" # hel*lo
# value = "aaa" # a*a*a
value = input()
result = pair_star(original_string=value, new_string="")
print(result)

