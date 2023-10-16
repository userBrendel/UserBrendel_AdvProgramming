import random

# A list for choices
choices = ["r", "p", "s", "q"]

# Looping using while / break / continue
print("Let's play Rock, Paper, Scissors!")
while True:
  UserChoice = input("\nr for rock \np for paper \ns scissors \nq for quit\n\nYour pick is: ")  # User input = pick

# If not (q)uit or invalid
  if UserChoice == "q":
    break  # Break loop

# Check if the user's choice is valid
  if UserChoice not in choices:
    print("Invalid choice. Please choose (r), (p), (s), or (q).")
    continue  # Restart the loop

# Generating computer choices
  ComputerChoice = random.choice(choices)
  print("Computer picked:", ComputerChoice)

# Possible outcomes || Game mechanics
  if UserChoice == ComputerChoice:  # A tie if random generates the same thing as the user.
   print("\nIT'S A TIE!\n------------------------")