'''
* * * * 
* * *
* *
*
Write a code to get row value from user and print the above star pattern.
'''

row = int(input("Enter row to print the patter :-"))
for i in range(row, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()