# Assignment: Type List
# Write a program that takes a list and prints a message for each element
# in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test
# its data type. If the item is a string, concatenate it onto a new string.
# If it is a number, add it to a running sum. At the end of your program print
# the string, the number and an analysis of what the array contains. If it
# contains only one type, print that type, otherwise, print 'mixed'.
#
# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
import numbers
# l = ['magical unicorns',19,'hello',98.98,'world']
# l = [2,3,1,7,4,12]
l = ['magical','unicorns']

numNumbers = 0
numbersTotal = 0
numStrings = 0
stringsTotal = ""

for thisObj in l:
    # print "Type=", type(thisObj)
    if isinstance(thisObj, numbers.Number):
        numNumbers += 1
        numbersTotal += thisObj
    elif isinstance(thisObj, str):
        numStrings += 1
        if numStrings == 1:
            stringsTotal += thisObj
        else:
            stringsTotal += " " + thisObj
    else:
        print "I dont' know what [" + thisObj + "] is."

if (numNumbers > 0) and (numStrings > 0):
    print "The array you entered is of mixed type"
    print "String: " + stringsTotal
    print "Sum: " + str(numbersTotal)
elif (numNumbers > 0):
    print "The array you entered is of numeric type"
    print "Sum: " + str(numbersTotal)
elif (numStrings > 0):
    print "The array you entered is of string type"
    print "String: " + str(stringsTotal)
else:
    print "The array you entered appears to be empty?"
