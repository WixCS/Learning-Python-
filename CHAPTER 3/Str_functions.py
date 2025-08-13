name = "prince"

print(len(name)) #Identify the length of string

print(name.endswith("nce"))

print(name.endswith("ncie"))

print(name.startswith("Pr"))

print(name.capitalize()) #Calpitalize the first letter only 

print(name.upper()) #Convert all letters to upper case

name1 = "Hello world"
index = name1.find("orld") 
print(index)

replace_word = name1.replace("world","Prince") #Swap the first word to the given word
print(replace_word)

text = "Nigga"
rep = text.count("g")#Tells the repeation of letter in the given word
print(rep)

txt = "a,b,c"
split = txt.split(",")# Split into a list
print(split)
