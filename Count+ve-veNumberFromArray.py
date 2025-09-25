#Count positive and negative elements from array

num = [1,2,3,4,5,-1,-2,-3,-4,9,8,7]
positiveCount = 0
negativeCount = 0
for i in num:
    if i < 0:
        negativeCount += 1
    else:
        positiveCount+=1
print("Positive number count from array :- ", positiveCount)
print("Negative number count from array :- ", negativeCount)

