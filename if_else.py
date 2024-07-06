# If Else Statement

a = int(input("Enter Your Age : "))
print("Your Age Is : ",a)
if(a >= 18):
    print("You Can Drive")
else:
    print("You Can Not Drive")     

# Elif Statement
    
num = int(input("Enter your number : "))
print("Your number is =",num)
if(num < 0):
    print("Your number is Negative.")
elif(num == 0):
    print("Your number is Zero.") 
else:
    print("Your number is Positive.")  

# Nested Statement 

n = int(input("Enter the number : "))
print("Your number is =",n)
if(n<5):
    print("Smaller than 5")
elif(n<30):
    if(n>20):
        print("Number is b/w 20-30")
    elif(n<20 and n>10):
        print("Number is b/w 10-20")
    else:
        print("Greater than 30")
else:
    print("Greater than 30")           