

def odd_even(startNum, endNum):

    for thisNum in xrange(startNum, endNum):
        if (thisNum % 2 == 0):
            numType = "even"
        else:
            numType = "odd"

        print "Number is {0}. This is an {1} number.".format(thisNum, numType)

# Call odd_even with start, end values
##odd_even(1, 2000)

def multiply(pList, pMult):
    newList = []
    for item in pList:
        newList.append(item*pMult)

    return newList
##

def layered_multiples(pList):
    newList = []
    for item in pList:
        newElementList = []
        for i in xrange(0, item):
            newElementList.append(1)

        newList.append(newElementList)

    return(newList)
##

##
#a = [2,4,10,16]
#print multiply(a, 5)
x = layered_multiples(multiply([2,4,5],3))
print x
