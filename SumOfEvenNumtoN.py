'''
Find the sum of all even number from 1 to n number
'''
n = int(input("Enter the number :- "))
i = 1
sum = 0
while(i<=n):
    if i % 2 == 0:
        sum = sum + i
    i = i+1
print(f"Sum of even number from 1 to {n} is :- {sum}")