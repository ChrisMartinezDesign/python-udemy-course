# ////////////////////
# Start
# -----
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(yourName, theirName):
    print(f"Hello {theirName}!")
    print(f"My name is {yourName}")
greet("Chris", "Josh")


#Write your code below this line 👇

def paint_calc(height, width, cover):
    can_amount = round((height * width) / cover)
    print(f"You will need {can_amount} cans.")


# //////////////////////////////////////
# Exercise 1 - Paint Area Calculator
# -----
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# /////////////////////////////////////
# Exercise 2 - Prime Number Checker
# -----
#Write your code below this line 👇

def prime_checker(number):
    for n in range(2, number):
        if number % n == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# ///////////////////////////
# Ceaser Cypher - Start 1
# -----
from art import logo

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

def ceaser_cypher(text, shift, direction):
    cypher = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabet:
            cypher += letter
            continue
        
        index = alphabet.index(letter)
        if index >= (25 - shift) and direction == "encode":
            index -= 26
            
        cypher += alphabet[index + shift]
        
    if direction != "encode" and direction != "decode":
        print(f"\nYou have not chosen Encode or Decode.")
    else:
        print(f"\nCypher: {cypher}")   

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

restart = True
while restart:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))
    shift = shift % 26

    ceaser_cypher(text, shift, direction) 

    restart = input("\nWould you like to run the Ceaser Cypher again? (yes/no) ") 
    if restart == "no":
        restart = False
        print("\nGoodbye!")


# ///////////////////////////
# Ceaser Cypher - Start 2
# -----
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)