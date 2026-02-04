# player1 = {
#     "health": 100,
#     "mana": 50,
#     "level": 3
# }

# print(player1["health"],player1["mana"],player1["level"])

# #1. Create a dictionary called book with keys: "title", "author", "year".
# # Print out the author’s name.

# book = {
#     "title" : "the fairy",
#     "author" : "nelson mandela", 
#     "year" : 2026
# }

# print(book["author"])

pass

# 2. Make a dictionary called grades with student names as keys and their scores as values.
# Write code to:
# Print a specific student’s score.
# Add a new student and score.
# Update an existing student’s score.

grades = {
    "Sophie": 90, 
    "Penelope": 80, 
    "Sol": 65, 
    "Karabo": 50
}
# print(grades["Sophie"], grades["Penelope"],grades["Sol"])
# grades["Simi"] = 45
# grades["Sophie"] = 90
# print(grades)
# grades = list(dict.keys(grades))      #also changed a dictionary to a list
# # print(grades[0])

# for grade in grades:
#     print(grade)


# my_keys = ["name", "age", "course"]
# my_values = ["Zizipo", 20, "Python Basics"]

# student_list = dict(zip(my_keys, my_values))
# print(student_list)

dict1 = {"a": 1, "b": 2}
dict2 = {"f": 3, "c" :4}

dict1.update(dict2)
dict1 = list(dict1.items())
dict1.sort()
print(dict1)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

