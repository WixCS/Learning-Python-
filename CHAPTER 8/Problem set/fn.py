# name = ["Prince","Nigga","Rohan"]
# cities = ["Patna","Pune","Mumbai","Delhi","Kerala"]
# food = ["Momo","Chowmien","Burger","Pizza"]

# def len_list(list):
#     print(len(list))

# len_list(name)
# len_list(cities)

# name = ["Prince", "Nigga", "Rohan"]
# cities = ["Patna", "Pune", "Mumbai", "Delhi", "Kerala"]

# def print_lists(list):
#    for item in list:
#       print(item, end=" ")

# print_lists(cities)

# To find the factorial

# n = int(input("Enter a number: "))

# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     print(fact)

# factorial(n)

#USD_INR

# def usd_inr(usd):
#     inr = usd * 85.60
#     print(usd,"USD =",inr,"INR")

# usd_inr(1)

# n = int(input("Enter a number: "))

# def odd_even(Value):
#     if(Value%2==0):
#         print("Even")
#     else:
#         print("Odd")

# odd_even(n)    

# def show (n):
#     if (n==0):
#         return 
#     print(n)
#     show(n-1)
    
# print(show(5))



cities = ["Patna","Pune","Mumbai","Delhi","Kerala"]

def print_list(list,index=0):
    if(index==len(list)):
        return
    
    print(list[index])
    print_list(list,index+1)
    
print_list(cities)