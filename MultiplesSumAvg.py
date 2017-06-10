# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000.
#     Use the for loop and don't use a list to do this exercise.
#
# Using xrange here. Seems like it's better behaved than range().
for x in xrange(1, 1000):
    # If remainder <> 0 then number is odd
    if x % 2 != 0:
        print x

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
x=5
# Kind of cheating with the loop by adding 1 to the total. Avoiding using <= comparison.
while x < 1000001:
    print x
    x += 5

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print "sum(a)=", sum(a) # Use the sum() function here. Pretty handy.

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
print "Avg(a)=", sum(a)/float(len(a))   # Make one of the numbers a FLOAT so it forces full division (ie: remainder)
