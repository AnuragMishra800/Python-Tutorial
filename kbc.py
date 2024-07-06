# Some dialauges from KBC 
print("Hello and welcome to KAUN BANEGA KARODPATI")
print("Apko 4 options diye jayenge har question pr aur apko simpaly bas to option shi lge us option ka index number press krna hai.")
print("Aur ye rha phla prashn apki screen pr")

# Asking Questions (No.1)
print("What is the national sports of India")
print("Aur ye rhe apke options")
print("1- Cricket\n2-Football \n3-Badminton\n4-Hockey")
answer = int(input("Enter Your Option:"))
print(f"Your Answer Is,{answer}")
if(answer==4):
    print("Congrats you won 1000rs.")
else:
    print("Oh No! Galat Jawab.")  

# Asking Questions (No.2)
print("What is the Prime Minister of India")
print("Aur ye rhe apke options")
print("1- Amit Shah\n2-Rahul Gandhi \n3-Narendra Modi\n4-Arvind Kejariwal")
answer = int(input("Enter Your Option:"))
print(f"Your Answer Is, {answer}")
if(answer==3):
    print("Congrats you won 10000rs.")
else:
    print("Oh No! Galat Jawab.") 

# Asking Questions (No.3)
print("What is the national anthem of India")
print("Aur ye rhe apke options")
print("1- Jan Gan Man\n2-Vande Mataram \n3-Abhi Tak Bna Hi Nhi.\n4-Mujhe Kya Pta.")
answer = int(input("Enter Your Option:"))
print("Your Answer Is,answer")
if(answer==1):
    print("Congrats you won 100000rs.")
else:
    print("Oh No! Galat Jawab.")  

# Game made by Harry 
questions = ["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the Prime Minister of India","Cricket","Football","Badminton","Hockey",4],["What is the national anthem of India","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4],["What is the national sports of India?","Cricket","Football","Badminton","Hockey",4] 
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,3200000]
money = 0
for i in range(0, len(questions)):
    question = questions[i] 
    print(f"Question for Rs.{levels[i]} is following:\n{question[0]}\n")  
    print(f"1-{question[1]}       2-{question[2]}")
    print(f"3-{question[3]}         4-{question[4]}\n")
    reply = int(input("Enter your answer: (1-4) or 0 to quit"))
    if(reply == 0):
        break 
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}\n")
        if(i==4): 
            money = 10000
        elif(i==8): 
            money = 320000
    else:
        print("Wrong Answer!\n")
        break
print(f"You can take money to your home is {money}") 