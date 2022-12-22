from sys import setrecursionlimit
setrecursionlimit(11000)

def solution(number_of_iterations):
    if number_of_iterations == 0:
        return 1
    result = solution(number_of_iterations=number_of_iterations-1)
    return result + 1/pow(2,number_of_iterations)

number_of_iterations = int(input())

print("%.5f" % solution(number_of_iterations))