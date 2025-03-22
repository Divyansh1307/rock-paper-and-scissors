rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
a=int(input("enter 0 for rock , 1 for paper and 2 for scissors\n"))
b=random.randint(0,2)
if a==0:
    print(rock)
elif a==1:
    print(paper)
elif a==2:
    print(scissors)
else:
    print("you lose wrong choose")
print("computer chose:\n")
if b==0:
    print(rock)
    if a==0:
        print("draw")
    elif a==1:
        print("you win")
    else :
        print("you lose")
elif b==1:
    print(paper)
    if a==0:
        print("you loss")
    elif a==1:
        print("draw")
    else :
        print("you win")
elif b==2:
    print(scissors)
    if a==0:
        print("you win")
    elif a==1:
        print("you loss")
    else :
        print("draw")

print(b)
