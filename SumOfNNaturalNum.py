'''
 Calculate and print the sum of the first n natural numbers.
'''

n = int(input("Enter the number :- "))
i = 0
sum = 0
while(i <= n):
    sum = sum + i
    i = i + 1
print(f"Sum of first {n} natural number is :- ",sum)

# n = int(input("Enter the number :- "))
# sum = 0
# for i in range(0, n+1):
#     sum = sum + i
#     i +=1
# print(sum)