# def recursion1(n):
#     print(n)
#     recursion2(2)
# def recursion2(n):
#     print(n)
#     recursion3(3)
# def recursion3(n):
#     print(n)
# recursion1(1)
def numbers(n):
    if n == 5:
        print(n)
        return 
    print(n)
    numbers(n+1)
numbers(1)


