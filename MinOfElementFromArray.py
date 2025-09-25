# find the minimum number from the arrya
num = [9,8,7,6,5,6,7,43,1]
min_num = num[0]
for i in num:
    if i < min_num:
        min_num = i
print(f"Minimum number from given array :- ",min_num)