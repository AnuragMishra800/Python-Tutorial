
#  Taking the input to match 
x = int(input("Enter the number: "))

# Matching the value 
match x:
    # All cases 
    case 0:
        print("x is zero.")
    case 10:
        print("x is ten.")
    case 100:
        print("x is hundred.")
    case _ if x==80:
        print("x is 80.")
    case _ if x!=900:
        print("x is not 900.")
    case _:
        print("X is",x)
        