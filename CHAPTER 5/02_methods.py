d = {} #empty dictionary 
marks = {              
    "Prince":100,      
    "Akash":56,
    "Rohan":45,
    90: "Rahul" 
    
}

print(marks.keys())
print(marks.values())

marks.update({"Prince":95,"Nigga":56} ) #Update the viden key value
print(marks)

print(marks.get("Alok")) #Print none 

#print(marks["Alok"]) #Return an error

print(marks.items()) #Gives in tuple form which is immutable

print(marks.pop("Rohan")) #Pop the value of given key

print(marks.popitem()) #removes the last key value pair

print(marks)
print(len(marks))