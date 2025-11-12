import random 

print("Welcome to the number guessing game.")

# Step 1: ask difficulty
level = input("Choose difficulty level (easy/hard): ").lower()
if level == 'easy':
  number_to_guess = random.randint(1,50)
  max_range = 50
elif level == 'hard':
  number_to_guess = random.randint(1,200)
  max_range = 200
else:
  number_to_guess = random.randint(1,100)
  max_range = 100

# Step 2: initialize variables
attempt = 0
history = []
while True:
  try:
    guess = int(input(f"Guess the number between 1 and {max_range}: "))
    attempt += 1
    history.append(guess)
    if guess < number_to_guess:
      print("Too Low!")
    elif guess > number_to_guess:
      print("Too High!")
    else:
      print(f"Congratulations! You guessed the number correctly in {attempt} attempts.")
      print(f"Your guesses were {history}")
      break
  except ValueError:
    print("Please enter valid number.")

    


