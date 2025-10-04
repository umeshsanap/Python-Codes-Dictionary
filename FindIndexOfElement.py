#Find index of an element in array
num = [1,2,3,4,5,6,7,8,9]
print(num)
findIndex = int(input("Enter the number from above array to find the index :- "))
if findIndex in num:
    print(f"Index of {findIndex} is : ",num.index(findIndex))
