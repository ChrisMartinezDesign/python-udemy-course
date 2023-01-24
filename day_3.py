# /////////////////
# Start
# -----
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

allowed_height = 120
ticket_price = 0

if height >= allowed_height:
  print("You can ride the rollercoaster!")
  
  age = int(input("How old are you? "))
  if age < 12:
    print("Child tickets are $5 ticket")
    ticket_price = 5
  elif age < 18:
    print("Youth tickets are $7 ticket")
    ticket_price = 7
  elif age >= 45 and age <= 50:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    print("Adult tickets are $12 ticket")
    ticket_price = 12

  photo_wanted = input("Would you like a photo for an additional $3? (yes/no) ")
  if photo_wanted == "yes":
    ticket_price += 3

  print(f"Your ticket will be ${ticket_price}")
else:
  print("Sorry, you have to grow more to ride the ride.")


# ///////////////////////
# Love Calculator
# -----
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = name1 + name2
lower_case_str = combined_names.lower()

t_counter = lower_case_str.count("t")
r_counter = lower_case_str.count("r")
u_counter = lower_case_str.count("u")
e_counter = lower_case_str.count("e")
l_counter = lower_case_str.count("l")
o_counter = lower_case_str.count("o")
v_counter = lower_case_str.count("v")

true_counter = t_counter + r_counter + u_counter + e_counter 
love_counter = l_counter + o_counter + v_counter + e_counter

score = int(str(true_counter) + str(love_counter))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


# ///////////////////////
# Treasure Island
# -----
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
answer1 = input("Would you like to go left or right? ").lower()
if answer1 == "left":
  print("Congradulations, you've chosen well!")
  answer2 = input("Would you like to swim or wait? ").lower()
  if answer2 == "wait":
    print("Nice job! That was a close one.")
    answer3 = input("Which door would you like to choose: Red, Blue, or Yellow? ").lower()
    if answer3 == "red":
      print("Game Over - You were burned by fire!")
    elif answer3 == "blue":
      print("Game Over - You were eaten by hairy beasts!")
    elif answer3 == "yellow":
      print("You Win! 🎉")
    else:
      print("Game Over")      
  else:
    print("Game Over - You were attacked by piranha!")
else:
  print("Game Over - You fell in a spike pit!")
