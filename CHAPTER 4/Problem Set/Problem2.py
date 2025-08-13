#Write a program to accept marks of 6 students and 
# int(display them in a sorted manner.

Marks = []

s1 = int(input("Enter the marks of Student 1: "))
Marks.append(s1)

s2 = int(input("Enter the marks of Student 2: "))
Marks.append(s2)

s3 = int(input("Enter the marks of Student 3: "))
Marks.append(s3)

s4 = int(input("Enter the marks of Student 4: "))
Marks.append(s4)

s5 = int(input("Enter the marks of Student 5: "))
Marks.append(s5)

s6 = int(input("Enter the marks of Student 6: "))
Marks.append(s6)

print("Marks arranged")
Marks.sort()
print(Marks)