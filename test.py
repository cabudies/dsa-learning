value = "abb"
print("value[0]=========", value[0])
print("value[1:3]=========", value[1:3])
print("value[3:]=========", value[3:])
# print("value[4]=======", value.get)

if (len(value)>=4) and (value[3]=='a'):
    print("valid")
else:
    print("invalid")

# print("value[-1]=========", value[-1])