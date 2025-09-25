#Count even and odd elements from array
num = [1,2,3,4,5,6,7,8,9,10,11]
evenCount = 0
oddCount = 0
for i in num:
    if i % 2 == 0:
        evenCount +=1
    else:
        oddCount += 1
print("Count for even number in given array :- ",evenCount)
print("Count for odd number in given array :- ",oddCount)