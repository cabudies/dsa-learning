# palindrome using recursion

# var = "racecar"
# result = True
# var = "gurjas"
# result = False

def palindrome_check(string):
    size = len(string)
    if size <= 1:
        return True
    if string[0] != string[size-1]:
        return False
    return palindrome_check(string[1:-1])

# string = input()
# string = "teet"
# string = "racecar"
string = "gurjas"

if palindrome_check(string):
    print('true')
else:
    print('false')


