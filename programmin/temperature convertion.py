temperatureValue=float(input("Enter temperature value: "))
unit=input("Enter unit in c or f: ")
if unit=="c":
    convert=(temperatureValue*9/5) + 32
    print("temperature in f: " + str(convert))
else:
    convert=(temperatureValue-32) * 5/9
    print("temperature in c: " + str(convert))
   
    
    