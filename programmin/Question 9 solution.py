#Vallary Atieno

number=int(input("Enter number: "))
if number<=1:
    print("not a prime number")
else:    
    for i in range(2,number):
    if(number%i==0):
        print("not a prime number")
        break
else:
    print("Prime number")
   