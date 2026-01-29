# Calculate your BMI using weight / (height ** 2) and print the result.
weight = 75
height = 1.5 
age = 18

bmi = weight / (height ** 2)
print(bmi)

# # Compare your age with 18 and print whether you are older or younger.

if age >= 18:
    print("you are older")
else:
    print("you are younger")

# # Use logical operators to check if your age is between 18 and 30.
if age >= 18 or age == 30:
    print("You are between 18 and 30 years")
else:
    print("You are below 18 and 19 years")
    
# # Write a program that checks if your BMI is in a healthy range (18–25).
if float(bmi) >= age:
    print("Your BMI is in a healthy range")
else:
    print("Your BMI is not in a healthy range")
    
# # Ask the user for their age and print whether they are a minor, adult, or senior.
# age = int(input("What is your age?: "))

if age >= 18:
    print("You are a senior")
elif age == 18:
    print("You are an adult")
else:
    print("You are a minor")


# # Write a program that checks if a password is "python123" and prints “Access granted” or “Access denied”.

password = "python123"

if password >= "":
    print("Access granted!")
else:
    ("Access denied!")
    
    
# Ask the user to enter two numbers and an operator (+, -, *, /).
# Use conditionals to perform the correct operation and print the result.
# Example: If the user enters +, add the numbers.


num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
operator = input("Enter an operator (+, -, *, /, %,  ): ")

if operator == "+":
    print("Result: ", num1 + num2)
elif operator == "-":
    print("Result: ", num1 - num2)
elif operator == "*":
    print("Result: ", num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Result: ", num1 / num2)
else:
    print("Invalid operator.")
    
    

# Try extending this calculator with these extra features:
# Division check → If the user tries to divide by zero, print "Error: Cannot divide by zero."
# Power operator → Add support for ^ (exponentiation). Example: 2 ^ 3 = 8.
# Multiple operations → Let the user keep calculating until they type "exit".