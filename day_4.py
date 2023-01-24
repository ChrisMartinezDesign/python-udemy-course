# ////////////////////////
# Start - Randomization
# -----
# Mersenne Twister - randomization pattern used by Python
# Python Modules - broken up pieces of functionality to be used for programs
# import random

# randomInt = random.randint(0, 4)
# randomFloat = random.random() # 0.000000 -> 0.999999...
# randomNum = randomInt + randomFloat
# print(randomInt)
# print(randomFloat)
# print(randomNum)

# love_score = random.randint(0, 100)

# Lists - data structure - similar to arrays
#Starts at index 0 - 0 represents the offset from the beginning of the list
states_of_america = ["Indiana", "Florida", "Massachusetts", "South Carolina"]
print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[-1])
states_of_america[0] = "Utah"
print(states_of_america[0])
states_of_america.append("Puerto Rico")
states_of_america.extend(["Minnesota", "North Carolina"])
print(states_of_america)


# ////////////////////////
# Exercise 1
# -----
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

# Coin Flip
headsOrTails = random.randint(0, 1)
coinFlip = "Coin Flip: "
if headsOrTails == 1:
  coinFlip += "Heads"
else:
  coinFlip += "Tails"
print(coinFlip)

# Dice Roll
diceRoll = random.randint(1, 6)
print(f"Dice Roll: {diceRoll}")

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print("\nWelcome to Catan!\n---")
print(f"Dice 1: {dice1}")
print(f"Dice 2: {dice2}")
print(f"Roll: {dice1 + dice2}")

# Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[0][1])


# //////////////////////
# Heads or Tails
# -----
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
headsOrTails = random.randint(0, 1)
if headsOrTails == 1:
  print("Heads")
else:
  print("Tails")


# //////////////////////
# Banker Roulette
# -----
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_length = len(names)
choice_index = random.randint(0, names_length - 1)
print(f"{names[choice_index]} is going to buy the meal today!")


# //////////////////////
# Treasure Map
# -----
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
row = int(position[1]) - 1
col = int(position[0]) - 1
map[row][col] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# //////////////////////
# Rock-Paper-Scissors
# -----
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

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper, Scissors")
user_choice = input("What do you choose? (Rock, Paper, or Scissors) ").lower()

choices = ["rock", "paper", "scissors"]
computer_choice = choices[random.randint(0, 2)]
print(f"Your apponent chose {computer_choice[0].upper() + computer_choice[1:len(computer_choice)]}")

if user_choice == "rock" and computer_choice == "scissors":
  print("Congratulations, Rock beats Scissors, you win!")
elif user_choice == "paper" and computer_choice == "rock":
  print("Congratulations, Paper beats Rock, you win!")
elif user_choice == "scissors" and computer_choice == "paper":
  print("Congratulations, Scissors beats Paper, you win!")
elif user_choice == "rock" and computer_choice == "paper":
  print("Your apponent has beaten you, Paper beats Rock, you lose!")
elif user_choice == "paper" and computer_choice == "scissors":
  print("Your apponent has beaten you, Scissors beats Paper, you lose!")
elif user_choice == "scissors" and computer_choice == "rock":
  print("Your apponent has beaten you, Rock beats Scissors, you lose!")
elif user_choice == computer_choice:
  print(f"It's a tie! {user_choice[0].upper() + user_choice[1:len(user_choice)]} cancels {computer_choice[0].upper() + computer_choice[1:len(computer_choice)]}")
else:
  print("Unfortunately, that's not a valid choice.")