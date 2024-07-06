
import time
time = int(time.strftime('%H'))
time = int(input("Enter Hour:"))
print(time)

# A Program For Greeting According To Time 

if(time>=0 and time<12):
   print("Good Morning")
elif(time>=12 and time<17):
   print("Good After Noon")
elif(time>=17 and time<24): 
   print("Good Night") 

# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(0)))

# import time
# start_time = time.time()
# # some code to measure
# end_time = time.time()
# print(f"Elapsed time: {end_time - start_time} seconds")