#count occurence of element
num = [1,2,3,4,5,6,7,8,10,1,1,2,4,4,3]
elementOccuerence = 0
element = int(input("Enter the number :- "))
for i in num:
    if i == element:
        elementOccuerence+=1
print(f"{element} occured {elementOccuerence} time")