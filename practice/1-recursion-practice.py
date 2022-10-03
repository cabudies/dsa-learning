def power_value(base_number, power):
    if power == 0:
        return 1
    value = base_number * power_value(base_number, power - 1)
    return value

base_number, power = input().split()
base_number = int(base_number)
power = int(power)

result = power_value(base_number=base_number, power=power)
print(result)
