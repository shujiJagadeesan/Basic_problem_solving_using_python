import math
def find_all_factors_of_a_number(number):
    i = 1
    while i <= math.sqrt(number):
        if (number % i == 0):
            if (number / i == i):
                print(i,end=" ")
            else:
                print(i,int(number/i),end=" ")
        i+=1
number = 100
find_all_factors_of_a_number(number)