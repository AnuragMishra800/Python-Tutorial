
# Finally Keyword In Python
 
def func1():
    try:
        l = [1,3,5,7]
        i = int(input("Enter The Index:")) 
        print(l[i]) 
        return 1
    except:
        print("Some Error Occurred")
        return 0
    finally:
        print("I always executed.") 

# print("I always executed.")

x = func1() 
print(x) 