# Python program to check the number is prime or not without function
num = int(input("Enter a number: "))
if num > 1:
    if num == 2:
        print(num, "is a prime number")
    else:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
else:
    print(num, "is not a prime number")
