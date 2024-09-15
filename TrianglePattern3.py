'''
            *
        *   *
    *   *   *
*   *   *   *
Write a code to get row value from user and print the above star pattern.
'''

row = int(input("Enter row to print the pattern :- "))
for i in range(1, row+1):
    for j in range(row - i):
        print(" ", end="    ")
    for k in range(i):
        print("*", end="    ")
    print()