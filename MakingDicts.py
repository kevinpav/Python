# Create a function that takes in two lists and creates a single dictionary where
# the first list contains keys and the second values. Assume the lists will be of equal length.
#
# Your first function will take in two lists containing some strings. Here are two example lists:
# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

def make_dict(arr1, arr2):
    new_dict = {}
    # If arr2 longer than arr1, switch key:value
    if len(arr2) > len(arr1):
        new_dict = zip(arr2, arr1)
    else:
        new_dict = zip(arr1, arr2)

    return new_dict
##

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(name, favorite_animal)
