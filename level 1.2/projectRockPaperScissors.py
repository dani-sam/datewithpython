import random
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
gameImages = [rock,paper,scissors]

# code of  user choice section
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper & 2 for Scissors\n"))
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose")
else:
    print(gameImages[userChoice])

# code of computer choice section
    computerChoice = random.randint(0,2)
    print("computer choice \n")
    print(gameImages[computerChoice])

# code of result section

    if userChoice == 0 and computerChoice == 2:
        print("You win")                                                                                                     
    elif computerChoice == 0 and userChoice == 2:
        print('You lose')
    elif computerChoice > userChoice:
        print("You lose")
    elif userChoice > computerChoice:
        print("You win")
    elif computerChoice == userChoice:
        print("It is draw")



         


