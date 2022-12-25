def remove_duplicate(x):
    x_length = len(x)
    if x_length == 0 or x_length == 1:
        return x
    small_output = remove_duplicate(x[1:])
    if x[0] != x[1]:
        small_output = x[0] + small_output
    return small_output


# value = "aabccba" # abcba
value = "xxxyyyzwwzzz" # xyzwz
print(remove_duplicate(value))


