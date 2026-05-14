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
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_list = [rock,paper,scissor]


my_input = int(input("Enter Your choice 0 for rock,1 for paper,2 for scissor: "))
my_turn = game_list[my_input]

print(f"you choose: {my_turn}")



random_turn = random.randint(0,2)
computer_turn = game_list[random_turn]
print(f"computer chooses: {computer_turn}")


if computer_turn == my_turn:
    print("Game Draw")
elif random_turn == 0 and my_input == 2:
    print("You Lost the game")    
elif random_turn == 0 and my_input == 1:
    print("You won!!")
elif random_turn == 1 and my_input == 0:
    print("You lost")    
elif random_turn == 1 and my_input == 2:
    print("You won!!")
elif random_turn == 2 and my_input == 0:
    print("You Won!!")
elif random_turn == 2 and my_input == 1:
    print("You lost.")        
elif my_input >=3:
    print("You have typed a wrong input.")