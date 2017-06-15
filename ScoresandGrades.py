# Write a function that generates ten scores between 60 and 100.
#
# Each time a score is generated, your function should display what
# the grade is for a particular score. Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def give_grade(pScore):
    # Return letter grade based on passed in numeric score
    if pScore < 60:
        return("F")
    elif pScore < 70:
        return("D")
    elif pScore < 80:
        return("C")
    elif pScore < 90:
        return("B")
    else:
        return("A")
##
import random
print "Scores and Grades"
for grade in xrange(1, 10):
    currScore = random.randint(1,100)
    print "Score: {0}; Your grade is {1}".format(currScore, give_grade(currScore))

print "End of the program. Bye!"
