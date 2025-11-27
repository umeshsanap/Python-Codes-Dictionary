num = int(input("Enter the number :- "))
if num > 1:
    if num == 2:
        print(f"{num} is prime")
    else:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is not prime number")
                break
        else:
            print(f"{num} prime number")
else:
    print(f"{num} is not prime")