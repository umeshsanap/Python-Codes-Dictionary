'''
write a python program which accept the number and print there table.
'''
num = int(input("Enter the number :- "))
for i in range(1, 11):
    print(f"{num} * {i} = ", num * i)