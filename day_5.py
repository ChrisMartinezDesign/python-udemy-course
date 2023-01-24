# /////////////////
# Start
# -----
# fruits = ["Apple", "Peach", "Pear"]
# pies = []
# for fruit in fruits:
#   print(fruit)
#   pies.append(f"{fruit} Pie")
# for pie in pies:
#   print(pie)

sum = 0
# You must go one over your desired range
# Add a third parameter to create a step through the loop: i.e. step by 3
for number in range(0, 101):
  sum += number
print(sum)


# /////////////////
# Exercise 1
# -----
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
length = 0

for height in student_heights:
  sum += height
  length += 1
  
if length != 0:
  average = sum / length
  print(f"Average Height: {average:.2f}")
else:
  print("Provide some values to get the average.")


# /////////////////
# Exercise 2
# -----
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# Sample Input - 78 65 89 86 55 91 64 89
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")


# /////////////////
# Exercise 3
# -----
#Write your code below this row 👇
evenSum = 0
for evenNumber in range(2, 101, 2):
  evenSum += evenNumber
print(f"The sum of the even numbers is {evenSum}")


# /////////////////
# Exercise 4
# -----
#Write your code below this row 👇
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)


# //////////////////////
# Password Generator
# -----
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for number in range(1, nr_letters + 1):
  password.append(random.choice(letters))
for number in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
  password.append(random.choice(numbers))

random.shuffle(password)
  
print(f"Here is your password: {''.join(password)}")
