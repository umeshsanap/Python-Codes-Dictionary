#Insert element at given position
num = [1,2,3,4,5]
enterIndex = int(input("Enter the position where we have to insert the element :- "))
enterElement = int(input("Enter new element :- "))
num.insert(enterIndex, enterElement)
print(num)