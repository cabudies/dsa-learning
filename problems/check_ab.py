from sys import setrecursionlimit
setrecursionlimit(11000)

def ab_check(string):
    string_len = len(string)
    if string_len == 0:
        return True

    if string[0] == 'a':
        if (len(string[1:])>1) and (string[1:3] == 'bb'):
            return ab_check(string[3:])
        else:
            return ab_check(string[1:])        
    else:
        return False
    
value = input()
if ab_check(value):
    print('true')
else:
    print('false')

