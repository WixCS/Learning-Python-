#Spam detector

s1 = "Make a lot of money"
s2 = "buy now"
s3 = "click this"
s4 = "subscribe this"

comment = input("Enter your comment: ")

if((s1.lower() in comment.lower()) or (s2.lower() in comment.lower()) 
   or (s3.lower() in comment.lower()) or (s4.lower() in comment.lower())):
    print("This is a spam")

else:
    print("This is not a spam")
