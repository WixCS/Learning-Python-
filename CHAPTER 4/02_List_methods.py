friends = ["Prince","Rohan",5,25.36,False,"Kevin"]
print(friends)
friends.append("Nigga")#add the string at the ends
print(friends)

num = [1,34,53,99,3,4,14]
num.sort() #Arrange in ascending order
print(num)

num.reverse() #reverse the given list

num.insert(3,69) #Insert the value 69 at the index 3 in the list

num_ = [1,24,56,78,3,20]
value = num_.pop(3) #Remove the given index and return the value
print(value)
print(num_)

num1 = [1,53,44,78,6] 
num1.remove(53) #Remove the value from list
print(num1)