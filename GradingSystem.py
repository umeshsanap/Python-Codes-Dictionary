marks = int(input("Enter the marks to check the grade :-"))
if marks >= 90:
    print("Grade : A")
elif marks == 80 and marks < 90:
    print("Grade : B")
elif marks == 70 and marks < 80:
    print("Grade : C")
elif marks == 60 and marks < 70:
    print("Grade : D")
elif 35 <= marks <= 60:
    print("Grade : E")
else:
    print("You are fail")