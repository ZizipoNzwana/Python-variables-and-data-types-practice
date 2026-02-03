# Write a program that asks the user for a password.
# If the password is "python123", print "Access granted."
# Otherwise, print "Access denied."
# password = 'python123'

# if password >= '':
#     print("Access Granted!")
# else:
#     print("Access denied!")


# number = int(input("Enter the number: "))

# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# def do_not_panic(n):
#     if n % 2 == 0:
#         print("Even number")
#         return n
#     else:
#         print("Odd number")
#         return n
    
# print(do_not_panic(3))

def reverse_words(sentence):
    sentence_list = sentence.lower().strip(" ")

    for char in sentence_list:
        return reversed(char)
        
print(reverse_words("Hello world"))




