num = int(input("Enter integer number to check number is Even or Odd:- "))
if num > 0:
    if num % 2 == 0:
        print(f"{num} is Even number")
    else:
        print(f"{num} is Odd number")
else:
    print(f"{num} is not greater than Zero.")