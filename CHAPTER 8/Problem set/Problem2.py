def temperature(C):
    Fahrenheit = ((9/5)*C) + 32
    return f"Temperature in Fahrenheit is {Fahrenheit}"

C = int(input("Enter temperature in celsius: ")) 
a = temperature(C)

print(f"{a}°F")