def to_find_GCD(number_1,number_2):
    if number_1 == 0:
        return number_2
    if number_2 == 0:
        return number_1
    while number_1 != number_2:
        if(number_1 > number_2):
            number_1 = number_1 - number_2
        else:
            number_2 = number_2 - number_1

    return number_1
n1 = 0
n2 = 20
greatest_common_divisor = to_find_GCD(n1,n2)
print(greatest_common_divisor , "is the greatest common divisor")