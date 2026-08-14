'''
Find the sum of all odd number from 1 to n
'''
n = int(input("Enter the number :- "))
sum = 0
i = 1
while(i<=n):
    if i % 2 != 0:
        sum = sum + i
    i += 1
print(f"Sum of all odd number from 1 to {n} is {sum}")