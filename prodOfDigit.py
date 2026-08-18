'''
Find and print the product of all digits of a given number.
ex. 123 = 1*2*3 = 6
'''

num = int(input("Enter the number :- "))
prod = 1
while(num>0):
    digit = num%10
    prod = prod * digit
    num = num//10
print(prod)