#Make a program for students enter their marks in 33% subjects and 
#passing marks is 33 and over all marks should br 40%

m1 = int(input("Enter your marks out of 100 in subject 1: "))

m2 = int(input("Enter your marks out of 100 in subject 2: "))

m3 = int(input("Enter your marks out of 100 in subject 3: "))

percentage = (m1+m2+m3)/3

    
if((m1<0 or m2<0 or m3<0) or (m1>100 or m2>100 or m3>100)):
    print("Invalid marks")
    
    
elif(m1 <33 and m2 >=33 and m3 >=33): 
    print("""You have been failed because,\nyou have less then 33 marks in Subject 1""")
    
elif(m1 >=33 and m2 <33 and m3 >=33): 
    print("""You have been failed because,\nyou have less then 33 marks in Subject 2""")
    
elif(m1 <33 and m2 >=33 and m3 <33):
    print("""You have been failed because,\nyou have less then 33 marks in Subject 3""")

elif((m1>=33 and m2>=33 and m3>=33) or (percentage >= 40)):
    print("You have been passed",percentage)
    
elif(0 <= percentage < 40):
    print("You have been failed \nyou have less than 40% marks over all ")
    
    


 