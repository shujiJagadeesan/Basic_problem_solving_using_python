def to_compute_power_of_number(number, exponent):
    if number == 0:
        return 0
    if exponent == 0:
        return 1
    result = 1
    for i in range(1,exponent+1):
        result *= number
    return result
number = 10
exponent = 2
power_of_a_number = to_compute_power_of_number(number,exponent)
print(power_of_a_number)