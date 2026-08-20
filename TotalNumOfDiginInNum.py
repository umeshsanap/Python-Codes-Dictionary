'''
Count and print the total number of digits in a given number.
'''
num = int(input("Enter the number :-"))
class CountNum:
    def countDigit(self, num):
        if num == 0:
            print(f"Count of 0 is 1")
            # return
        else:
            og_num = num
            count = 0
            while(num >0):
                num = num // 10
                count = count + 1
            print(f"Count of {og_num} is {count}")
obj = CountNum()
obj.countDigit(num)
            