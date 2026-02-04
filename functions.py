# 1. Even or Odd Checker  
# Create a function that takes a number and returns whether it is "Even" or "Odd".

# def check_number(n):
#     if n % 2 == 0:
#         # print("Even")
#         return "Even"
#     else:
#         return "odd"

# print(check_number(10))

# 2. Greeting Function  
# Write a function that takes a person’s name and age, then prints a message like:
# "Hello Zizipo, you are 25 years old!"

# def greet(name, age):
#     return f"Hello, {name} you are {age} old!" 

# print(greet("Zizipo", 25))

# Temperature Converter  
# Write a function that converts Celsius to Fahrenheit.
# Formula: F = (C * 9/5) + 32

# def temperature_converter(celsius):
#     fahrenheit = (celsius * 9/5) + 2
#     celsius = fahrenheit
#     return celsius

# print(f" It is {temperature_converter(15)} degrees celsius hot! ")


# List Summation  
# Make a function that takes a list of numbers and returns the sum of all elements.
# def summation(numbers):
#     # total = 0
#     # for num in numbers:
#     #     total += num
#     # return total
# # print(summation([1, 2, 3, 4, 5]))
#     numbers = [1, 2, 3, 4, 5, 10]
#     return sum(numbers)
# print(summation(2))

# Word Counter  
# Write a function that takes a sentence and returns how many words are in it.

# def word_counter(sentence):
#     count = 0
#     sentence = sentence.lower().split(" ")
#     return count + len(sentence)

# print(word_counter("Hello world, Welcome to python"))


# Palindrome Checker  
# Create a function that checks if a word is a palindrome (same forwards and backwards, like "madam").

# def palindrome(word):
#     if word == word[::-1]:
#         return word
#         # print("it is a palindrome")
#     # else:
#     #     print("Not palindrome", )

# print(palindrome("madam"))


# Factorial Calculator  
# Write a function that calculates the factorial of a number (e.g., 5! = 5*4*3*2*1).

def factorial(number, n):
    count = 0
    while count != 1:
        if number * n:
            return count + 1
print(factorial(2, 2))
