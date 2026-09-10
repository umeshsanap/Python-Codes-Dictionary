'''
num = 153
Total digits (n) = 3
final output = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
if num == final output 
number is armstrong number
'''
num_str = input("Enter the number to check it is armstrong or not :- ")
len_num = len(num_str)
temp=0
num = int(num_str)
og_num = num
while(num >0):
    digit = num % 10
    temp = temp + digit**len_num
    num = num // 10

if og_num == temp:
    print(f"{og_num} is armstrong number")
else:
    print(f"{og_num} is not armstrong number")
