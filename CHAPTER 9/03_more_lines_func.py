str = open("file.txt")

more_lines = str.readlines() #It stores in list
print(more_lines, type(more_lines))
str.close()

#-----------------------------------------------------------------

line1 = str.readline() #It store's in string
print(line1, type(line1))

line2 = str.readline()
print(line2, type(line2))

line3 = str.readline()
print(line3, type(line3))

line4 = str.readline()
print(line4, type(line4))

str.close()

#-----------------------------------------------------------------

#Doing using loops

line = str.readline

while(line != ""):
    print(line)
    line = str.readline()

str.close()