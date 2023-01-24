#Data Types
print("Data Types")

# Subscripting
print("Hello"[2])

# Integers
print(type(1234))

# Float
print(type(1.234))

# Boolean
print(type(True))

# ---
print("-----")

# Type casting - convert one data type into another
print("Type Casting")
str = "3323"
int = int(str)
print(type(int))

# Order of Operations - PEMDASLR
print(3 * (3 + 3) / 3 - 3)

# Rounding
print(round(8 / 3, 5)) # Rounds the result to 5 decimal places
print(8 // 3) # Floor division - autimatically rounds the result to an int

# F-string
score = 0
height = 1.2
isWinning = True
print(f"your score is {score}, your height is {height}, {isWinning}")


# /////////////////////
# BMI Calculator
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)
intro_str = f"Your BMI is {bmi}, "

if bmi < 18.5:
    print(intro_str + "you are underweight.")
elif bmi <= 25:
    print(intro_str + "you have a normal weight.")
elif bmi <= 30:
    print(intro_str + "you are slightly overweight.")
elif bmi <= 35:
    print(intro_str + "you are obese.")
else:
    print(intro_str + "you are clinically obese.")



# /////////////////////
# Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator!")

bill = float(input("How much was your bill? $"))
tip = float(input("How much tip would you like to give? 10, 15, 20? ")) / 100
people_dining = int(input("How many people shared the meal? "))
tip_total = tip * bill
bill_total = bill + tip_total

bill_per_person = bill_total / people_dining

print(f"Each person should pay: ${bill_per_person:.2f} (includes tip)")