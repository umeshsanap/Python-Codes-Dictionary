'''
*
* *
* * *
* * * * 
Write a code to get row value from user and print the above star pattern.
'''

row = int(input("Enter number of rows to print the pattern :-"))
for i in range(1, row+1):
    for j in range(i):
        print("*", end=" ")
    print()