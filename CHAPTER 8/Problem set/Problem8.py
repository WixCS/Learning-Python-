def table(n):
    for num in range(1,11):
        print(f"{n} X {num} = {n*num}")
    return   

n = int(input("Enter a number: "))
table(n)