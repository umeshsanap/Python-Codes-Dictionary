num = int(input("Enter the number from where you want odd number :- "))
class OddNum:
    def findOddNum(n):
        i = 0
        sum = 0
        while(i<=n):
            if i%2!=0:
                sum = sum+i
            i += 1
        print(f"Sum of all odd number from {n} is {sum}")

obj = OddNum
obj.findOddNum(num)