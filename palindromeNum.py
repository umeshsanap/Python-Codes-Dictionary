num = int(input("Enter the number :- "))
digit = 0
reverseNum = 0
while(num > 0):
    digit = num % 10
    reverseNum = (reverseNum * 10)+digit
    num = num // 10

print(reverseNum)