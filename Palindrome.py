'''
Check whether the given number is a palindrome.
'''
num = int(input("Enter the number :- "))
og_Num = num
revNum = 0
while(num>0):
    reminder = num % 10
    revNum = (revNum * 10) + reminder
    num = num // 10
if num == revNum:
    print(f"The {og_Num} is palindrome...!")
else:
    print(f"The {og_Num} is not palindrome...!")