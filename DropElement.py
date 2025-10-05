# Delete element at given position
num = [1,2,3,4,5]
print("Given array :- ", num)
enterposition = int(input("Enter the element position(index of that element) :- "))
num.pop(enterposition)
print("array after deleting element :- ", num)