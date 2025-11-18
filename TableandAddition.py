'''
when user send number it will print there table
also addition from zero till that number
'''
num = int(input("Enter the number :- "))
sum = 0
print(f"Table for {num}")
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

for j in range(0, num+1):
    sum = sum + j
print(f"Total addition of number from {sum} to {num} is ",sum)