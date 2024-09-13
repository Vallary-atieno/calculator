temperature_value=float(input("enter Temperature value: "))
unit=input("Enter temperature unit in c or f: ")
ctof=(temperature_value*9/5)+32
ftoc=(temperature_value-32)*5/9
if unit=="c" or "celcius":
    print(f"{temperature_value}c is equivalent to {ctof:.2}f")
    
elif unit=="f":
    print(f"{temperature_value}f is equivalent to {ftoc:.2}c")
else:
    print("Invalid temperature unit please enter c or f")