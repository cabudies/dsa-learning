# n = 6
# n = 49
# n = 637759701
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count += 1

# print(count)

# A = 4
# prime = 1
# i = 2
# while i<A:
#     if A%i == 0:
#         prime = 0
#         break
#     i += 1

# print("prime=======", prime)

import math

A = 1332
# sqrt_value = math.sqrt(A)
# print(sqrt_value)

sqrt_value = int(math.sqrt(A))

print((sqrt_value * sqrt_value) == A)


