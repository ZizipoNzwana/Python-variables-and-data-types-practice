# Ask the user for their age and classify them:
# If age is less than 13 → "You are a child."
# If age is between 13 and 19 (inclusive) → "You are a teenager."
# If age is 20 or above → "You are an adult."

age = int(input("What is you age? : "))

if age <=13:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a teenager")
elif age >= 20:
    print("you are an adult")
    