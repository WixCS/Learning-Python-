'''
***
**
*
'''

def star(n):
    if(n==0):
        return
    
    print("*" * n)
    star(n-1)

n = int(input("Enter the number: "))   

star(n)

    
