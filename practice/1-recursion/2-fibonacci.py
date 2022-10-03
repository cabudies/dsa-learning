def fun(n):
    print("n====", n)
    if(n == 4):
        return n
    else:
        return 2*fun(n+1)


print(fun(2))