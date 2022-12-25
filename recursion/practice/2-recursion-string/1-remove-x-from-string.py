# Problem: Remove x from string
def removeX(string): 
    if len(string) == 0:
        return string
    small_string = removeX(string[1:])
    if string[0] == "x":
        return "" + small_string
    else:
        return string[0] + small_string
    
# Main
string = input()
print(removeX(string))