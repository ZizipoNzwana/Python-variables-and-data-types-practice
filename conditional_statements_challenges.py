# Exercise_1- Age classifier

# Ask the user for their age and classify them:
# If age is less than 13 → "You are a child."
# If age is between 13 and 19 (inclusive) → "You are a teenager."
# If age is 20 or above → "You are an adult."

age = int(input("What is your age? : "))

if age <=13:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20:
    print("you are an adult")
pass

# # Exercise _2- Number Range Checker
# # Write a program that asks for a number:
# # If the number is between 1 and 100 (inclusive), print "Valid number."
# # Otherwise, print "Out of range."

number = int(input("Enter a number: "))

if number >= 1 and number < 100 +1:
    print("Valid number")
else:
    print("Out of range")
pass
# Exercise_3-Login system
# # Ask the user for a username and password:
# # If username is "admin" and password is "1234", print "Login successful."
# # Otherwise, print "Login failed."
user_name = input("What is your user name? ")
pass_word = input("Enter your password: ")

if user_name.lower() == "admin" and pass_word == "1234":
       print("Login successful")
else:
    print("Login failed")
    
# Exercise_4-Divisibility Test
pass
# Ask the user for a number:
# If the number is divisible by both 3 and 5 → "FizzBuzz"
# If divisible by only 3 → "Fizz"
# If divisible by only 5 → "Buzz"
# Otherwise → "Not divisible by 3 or 5"
    
number = int(input("Enter a number: "))

if number % 3 and number % 5:
    print("FizzBuzz")
elif number % 3:
    print("Fizz")
elif number % 5:
    print("Buzz")
else:
    print("not divible by 3 or 5")
    
pass
# Exercise_5-Scholarship Eligibility
# Ask the user for their grade (0–100) and attendance percentage:
# If grade is above 85 and attendance is above 90 → "Eligible for scholarship."
# If grade is above 85 or attendance is above 90 → "Partially eligible."
# Otherwise → "Not eligible."

student_grade = int(input(" Enter your grade mark: "))

if student_grade >= 85 and student_grade >= 90:
    print(" You are eligible for scholarship")
elif student_grade >= 85 or student_grade >= 90:
    print("You are partially eligible for scholarship")
else:
    print("You are not eligible")