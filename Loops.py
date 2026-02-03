# Challenge 1: Print Numbers
# Write a for loop that prints numbers from 1 to 10.
# for num in range(1, 11):
#     print(num)

# Challenge 2: Multiplication Table
# Ask the user for a number, then use a for loop to print its multiplication table up to 10.

# numbers = int(input("Enter a number: "))
# for num in range(10, 0, -1):
#     num * numbers
#     print(f"{numbers} x {num} = {num *numbers}")
# # total = 1
pass
# Challenge 2: Sum of Numbers
# Use a for loop to add up all the numbers from 1 to 100 and print the total.

# numbers = [ 3, 4, 5, 6]
# for num in numbers:
#     total *= num
# print(total)
pass
# Challenge 3: Count Vowels
# Write a program that loops through the string "programming" and counts how many vowels (a, e, i, o, u) are in it.

# sentence = "programming"
# vowels = "aeiou"
# count = 0

# for vowel in sentence:
#     sentence = sentence.lower()
#     if vowel in vowels:
#         count += 1
# print(count)
pass 
# Challenge 5: Reverse a Word
# Ask the user to enter a word. Use a for loop to print the word backwards.
# Example: "hello" → "olleh"

# sentence = input("Enter sentence: ")

# for word in sentence:
#     word = sentence[::-1].lower()
# print(word)

pass
# WHILE LOOPS....
# Challenge 1: Countdown
# Write a program that starts at 10 and counts down to 1 using a while loop. After reaching 1, print "Blast off!".

# count = 10
# while count >= 1:
#     print(count)
#     count = count -1
# print("Blast off!")
pass

# password = ""
# while password.lower() != "python123":
#     password = input("Enter password: ")
# print("Acess granted!")

pass
# Challenge 2: Guess the Number
# Pick a secret number (e.g., 7).
# Ask the user to guess the number.

# secret_number = 5

# while secret_number >= 1:
#     guess_number = int(input("Enter your guessing number: "))
#     if secret_number != guess_number:
#         print("Try again!")
#     else:
#         print("You got it!")
#         break

pass
# # Challenge 3: Sum Until Zero
# # Ask the user to enter numbers.
# # Keep adding them together until the user enters 0.
# # Then print the total sum.

# number = input("Enter your number: ").split()

# print(type(number))
# num = 0
# total = 0
# while num < len(number):
#     total += int(number[num])
#     num = num + 1
# print(total)
    
    
# numbers = [ 1, 2, 6, 4]
# total = 0
# for num in range(0, len(numbers)):
#     total += numbers[num]
# print(total)
    

def count_word_occurrences(list_of_words):
    result : dict = {}
    # result.get()
    
    for word in list_of_words:
        if result.get(word, None):
            result[word] += 1
        else:
            result[word] = 1
    return result

print(count_word_occurrences(["apple", "banana", "apple", "orange"]))