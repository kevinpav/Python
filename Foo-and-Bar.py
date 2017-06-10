# Optional Assignment: Foo and Bar
# Write a program that prints all the prime numbers and all the perfect
# squares for all numbers between 100 and 100000.
#
# For all numbers between 100 and 100000 test that number for whether it
# is prime or a perfect square. If it is a prime number print "Foo".
# If it is a perfect square print "Bar". If it is neither print "FooBar".
# Do not use the python math library for this exercise. For example, if
# the number you are evaluating is 25, you will have to figure out if it
# is a perfect square. It is, so print "Bar".
#
# This assignment is extra challenging! Try pair programming and pulling up a white board.

startNum = 100
endNum = 100000

for thisNum in xrange(startNum, endNum):
    maxDiv = thisNum / 2    # Can't use math.sqrt()
    for div in xrange(2, maxDiv+1):
        # If remainder is zero, not prime
        if (thisNum % div == 0):
            # Test if perfect square
            if (thisNum/div == div):
                print "FooBar:", thisNum, "(", div, ")"
            break   # Not prime
        elif (div == maxDiv):
            print "Foo:", thisNum    # We have a prime#
