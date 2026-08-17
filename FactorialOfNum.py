'''
n! = n * (n-1) * (n-2) * (n-3)*....*1 
'''

num = int(input("Enter the number to find factorial :- "))
class Factorial:
    def factorialOfNum(n):
        if n < 0:
            print(f"factorial of {n} is not possible")
        if n == 0:
            print(f"factorial of {n} is 1")
        i = n
        numFact = 1
        while(i>0):
            numFact *= i
            i -=1
        print(f"factorial of {n} is {numFact}")

obj = Factorial
obj.factorialOfNum(num)