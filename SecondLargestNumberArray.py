# Write a python program which finds the second largest number in an array.
n = int(input("Enter how many number you want in your array:-"))
arr = []
for i in range(n):
    numbers = int(input(f"Enter number:-"))
    arr.append(numbers)
if len(arr) >1:
    arr.sort()
    second_largest = arr[-2]
    print("Second largest number in array is:-",second_largest)
else:
    print("Array do not have sufficient elements to find Second largest number")