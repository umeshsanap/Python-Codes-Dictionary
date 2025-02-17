print('''
+ Addition
- Substraction
* Multiplication
/ Divide''')
operation = input("Enter the operation : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if operation == '+' or operation == "Addition":
    print("Addition of ",num1," and ",num2," is :", num1 + num2)
elif operation == '-' or operation == 'Substraction':
    print("Substraction of ",num1," and ",num2," is :", num1 - num2)
elif operation == '*' or operation == 'Multiplication':
    print("Multiplication of ",num1," and ",num2," is :", num1 * num2)
elif operation == '/' or operation == 'Divide':
    print("Divide of ",num1," and ",num2," is :", num1 / num2)
else:
    print("Operation not occured")