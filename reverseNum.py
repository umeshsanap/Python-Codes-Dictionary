n = int(input("Enter the number :- "))
revNum = 0
while n > 0:
    digit = n % 10
    revNum = revNum * 10 + digit
    n = n // 10
print(revNum)