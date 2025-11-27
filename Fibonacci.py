'''
Write a python program which print the fibonacci series upto entered number.
'''
n = int(input("Enter the number :- "))
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        print(a, end = " ")
        a, b = b, a+b

obj = fibonacci(n)