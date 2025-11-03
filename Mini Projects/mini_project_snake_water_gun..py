import random

SNAKE = 's'
WATER = 'w'
GUN = 'g'
emojis = {SNAKE: '🐍', WATER: '💧', GUN: '🔫'} 
choices = tuple(emojis.keys())

def get_user_choice():
  while True:
    user_choice = input('Snake, Water or Gun? (s/w/g): ').lower()
    if user_choice in choices:
      return user_choice
    else:
      print('Invalid choice!') 

def display_choices(user_choice, computer_choice):    
  print(f"You chose: {emojis[user_choice]}")
  print(f"Computer chose: {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
      print("Tie")
    elif (
    (user_choice == SNAKE and computer_choice == WATER) or 
    (user_choice == WATER and computer_choice == GUN) or 
    (user_choice == GUN and computer_choice == SNAKE)):
      print("You win! 🎉")
    else:
      print("You lose! 😢")  

def play_game():
  while True:
      user_choice = get_user_choice()
      computer_choice = random.choice(choices)
      display_choices(user_choice, computer_choice)
      determine_winner(user_choice, computer_choice)
      should_continue = input("Do you want to play again? (y/n): ").lower()
      if should_continue == 'n':
        break

play_game()


  


  

