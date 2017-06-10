# Assignment: Find Characters
# Write a program that takes a list of strings and a string containing a single
# character, and prints a new list of all the strings containing that character.
#
# Here's an example:

# input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for word in word_list:
    if char in word:
        new_list.append(word)

print new_list
