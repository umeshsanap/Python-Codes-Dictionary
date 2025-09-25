#find max number from array
num = [1,3,5,7,9,10,18]
max_num= num[0]
for i in num:
    if i > max_num:
        max_num = i
print(f"{max_num} is maximum number from the array.")        