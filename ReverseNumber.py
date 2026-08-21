'''
Reverse the given number and print the reversed value.
'''
num = int(input("Enter the number :- "))
rev = 0
while(num>0):
    reminder = num % 10
    rev = (rev * 10) + reminder
    num = num // 10 
print(rev)