# While Loop In Python 

n = int(input("Enter the number between 90-100: "))
while(n<=100 and n>=90):
    n = int(input("Guess Again: "))
    print("Your number is between 90 and 100")
    if(n==96): 
        print("Congrats you guess the right number") 
print("Over") 

count = 10
while(count>0):
    print(count)
    count = count-1 

count = 1
while(count<21):
    print(count)
    count = count+1
else:
    print("Khatam Tata Bye Bye.") 