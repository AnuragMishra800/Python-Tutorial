# Enumerate Function In Python 
# Normal 
marks = [1,34,65,3,55,99,23,54,24]
index = 0
for mark in marks:
    print(mark)
    if(index == 5):
        print("Bhot shi yar!")
    index+=1

# With Enumerate 
marks = [1,34,65,3,55,99,23,54,24]
for ind, mark in enumerate(marks):
    print(mark)
    if(ind == 5):
        print("Bhot shi yar!")

series = {'Squid Games', 'Money Heist', 'Game Of Thrones', 'Breaking Bad', 'Stranger Things'}
for index,series in enumerate(series):
    print(index, series) 

series = ('Alice In Borderland', 'See', 'Sweet Home', 'House Of Dragons', 'Withcer')
for index,series in enumerate(series, start=1): 
    print(index, series) 