# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
def draw_stars1(pList):
    for item in pList:
        print "*" * item

##
x1 = [4, 6, 1, 3, 5, 7, 25]
draw_stars1(x1)

# Part II
# Modify the function above. Allow a list containing integers and strings to be
# passed to the draw_stars() function. When a string is passed, instead of
# displaying *, display the first letter of the string according to the
# example below. You may use the .lower() string method for this part.
def draw_stars2(pList):
    for item in pList:
        if isinstance(item, int):
            print "*" * item
        else:
            print item[0].lower() * len(item)

##

x2 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x2)
