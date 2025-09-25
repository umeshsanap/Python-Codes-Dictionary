#reverse the array element
num = [90,80,70,60,50,40,30,20,10]
reverseArray = []
i = len(num) - 1
while i >=0:
    reverseArray.append(num[i])
    i -= 1
print("Regular array :- ",num)
print("Reverse version of the given array is :-",reverseArray)