m1 = int(input("Enter your marks out of 100 in subject 1: "))

m2 = int(input("Enter your marks out of 100 in subject 2: "))

m3 = int(input("Enter your marks out of 100 in subject 3: "))

percentage = (m1+m2+m3)/3

#Valid score value
if(m1<0 or m2<0 or m3<0):
    print("Enter valid marks")
    
elif(m1>100 or m2>100 or m3>100):
    print("Enter valid marks")

elif(100>=percentage>=40 and 100>=m1>=33 and 100>=m2>=33 and 100>=m3>=33):
    print("Congrats! You are passed",percentage)

else:
    print("You are failed,try again next year!",percentage)
