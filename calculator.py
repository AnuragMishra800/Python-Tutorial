
# Taking Inputs From The User

n1 = int(input("Enter Number 1 : "))
n2 = int(input("Enter Number 2 : "))

# Showing Selected Input Value To User

print("Your Entered Number 1 is",n1)
print("Your Entered Number 2 is",n2)

# Taking Operations Input From The User

print("Press 1 For Addition.\nPress 2 For Subtraction.\nPress 3 For Multiplication.\nPress 4 For Division.")

entered_number = int(input("Choose any number from 1 to 4 :"))

# Applying Operations According To The Selection Of The User

if(entered_number==1):
    print("Your result is",n1+n2) 
elif(entered_number==2):
    print("Your result is",n1-n2) 
elif(entered_number==3):
    print("Your result is",n1*n2) 
elif(entered_number==4):
    print("Your result is",n1/n2) 
else:
    print("Invalid Number Choosen.Please Retry.") 