marks = int(input("Enter you marks: "))
if(marks<0):
    print("Enter valid score")
    grade = "not valid"
elif(marks>100):
    print("Enter valid score")
    grade = "not valid"

if(marks<=100 and marks>=90):
    grade = "Ex"
if(marks<90 and marks>=80):
    grade = "A"
if(marks<80 and marks>=70):
    grade = "B"
if(marks<70 and marks>=60):
    grade = "C"
if(marks<60 and marks>=50):
    grade = "D"
elif(marks<50 and marks>=0):
    grade = "F"
    
print("Your grade is", grade)