f = open("file.txt")

data = f.read()
print(data)
f.close()

#The same can be done using with statement

with open("file.txt") as f:
    print(f.read())

#No need to close the opened file using with