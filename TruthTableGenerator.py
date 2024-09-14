val1 = input("Which truth table you want? :-")
if val1 == 'and':
    print("Truth table for and ")
    print("True and True = True")
    print("True and False = False")
    print("False and True = False")
    print("False and False = False")

elif val1 == 'or':
    print("Truth table for or ")
    print("True or True = True")
    print("True or False = True")
    print("False or True = True")
    print("False or False = False")

elif val1 == 'not':
    print("Truth table for not")
    print("Not True = False")
    print("Not False = True")

else:
    print("Print table not available")