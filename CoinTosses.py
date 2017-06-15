# Write a function that simulates tossing a coin 5,000 times. Your function
# should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!

def coinToss():
    import random
    numHeads, numTails = 0, 0
    headsOrTails = ""
    for thisToss in xrange(1, 5001):
        coinFlip = random.randint(1,2)
        if coinFlip is 1:
            headsOrTails = "head"
            numHeads += 1
        else:
            headsOrTails = "tail"
            numTails += 1

        print "Attempt #{0}: Throwing a coin... It's a {1}! ... got {2} head(s) so far and {3} tails(s) so far".format(thisToss, headsOrTails, numHeads, numTails)

##

print "Starting the program..."
coinToss()
print "Ending the program, thank you!"
