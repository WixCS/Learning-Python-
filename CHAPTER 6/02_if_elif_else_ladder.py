age  = int(input("Enter your age :"))

#if elif else ladder

if(age>=18):
    print(f"Your age is {age},You are an adult")
    print("Thank you")

elif(age<0):
    print("You entered an invalid age")
    print("Thank you")

elif(age==0):
    print("You entered 0 which in not a valid age")
    print("Thank you")

else:
    print(f"Your age is {age},You are not an adult")
    print("Thank you")