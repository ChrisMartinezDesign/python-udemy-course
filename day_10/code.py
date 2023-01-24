# ////////////////////////
# Start
# -----
# Functions with Outputs

first_name = input("What's your first name: ")
last_name = input("What's your last name: ")
formatted_name = ""

def format_name(f_name, l_name):
    # Docstring
    """
    Receives a first and last name and then formats them into a full name
    """
    if f_name == "" or l_name == "":
        return
        
    return f'{f_name.title()} {l_name.title()}'

formatted_name = format_name(first_name, last_name)

print(formatted_name)


# /////////////////////////////
# Exercies 1 - Days in Month
# -----
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if is_leap(year) and month == 2:
      return 29
  return month_days[month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# ////////////////////////
# Calculator 
# -----
from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Operations Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Creates a string of all posible operands
operands = ""
for operand in operations:
    if operand == list(operations)[-1]:
        operands += operand
    else:
        operands += f'{operand} '

def calculator():
    print(logo)
    number1 = float(input("Please enter your first number: "))
    
    shouldContinue = True
    while shouldContinue:
        print(operands)
        operation = input("Which operation would you like to perform?: ")
        number2 = float(input("Please enter your second number: "))
    
        operationFunction = operations[operation]
    
        result = operationFunction(number1, number2)
    
        print(f'{number1} {operation} {number2} = {result}')

        condition = input(f'Type "yes" to continue with {result}\nType "new" to start a new calculation\nType "no" to exit: ').lower()
        if condition == "yes":
            number1 = result
        elif condition == "new":
            calculator()
        else:
            return

calculator()
