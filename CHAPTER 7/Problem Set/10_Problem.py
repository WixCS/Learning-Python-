#Write a program to print multiplication table of n using for loops in reversed 
# order.

num = int(input("Enter any number: "))

for i in range(1,11):
    print(f"{num} x {11-i} = {num*(11-i)} ")


i = 10

while(0<i<11):
    print(f"{num} x {i} = {num*i} ")
    i -= 1
