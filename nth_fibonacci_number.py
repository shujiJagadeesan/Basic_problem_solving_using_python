def nth_fibonacci_number(n):
    if n < 0:
        print("Incorrect output")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci_number(n-1)+nth_fibonacci_number(n-2)
n = 9
nth_fibo_num = nth_fibonacci_number(n)
print(nth_fibo_num)