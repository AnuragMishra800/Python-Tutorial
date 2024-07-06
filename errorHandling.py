
# Exception Handling In Python 

a = input("Enter A Number:")
print(f"Mulplication Table Of {a} is:")
try:
    for i in range(1,11):
       print(f"{int(a)} X {i} = {int(a)*i}")  
# except Exception as e:
#     print(e)
except:
    print("Sorry! Invalid Input Error Ocuured.") 
print("Task Done")
print("End Of Program") 

try:
    num = int(input("Enter An Integar:"))
    a = [3, 4] 
    print(a[num]) 
except ValueError:
    print("Number Entered Is Not An Integar.") 
except IndexError:
    print("Index Error") 