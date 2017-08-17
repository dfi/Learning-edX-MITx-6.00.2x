import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.figure("test")
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    
    def longest_run(L):
        longest_run = 0
        i = 0
        while i < len(L):
            run = 1
            for j in range(i, len(L)-1):
                if L[j+1] == L[j]:
                    run += 1
                else:
                    i = j + 1
                    break
            else:
                i += 1
            
            if longest_run < run:
                longest_run = run
        return longest_run            
    
    runs = []
    for t in range(numTrials):
        rolls = []
        for i in range(numRolls):
            rolls.append(die.roll())
        run = longest_run(rolls)
        runs.append(run)

    makeHistogram(runs, 10, "Longest run", "Number of longest run", 
                  "Longest Runs Distribution")
    
    mean, std = getMeanAndStd(runs)
    return mean
    
    
#==============================================================================
# def longest_run(L):
#     longest_run = 0
#     i = 0
#     while i < len(L):
#         run = 1
#         for j in range(i, len(L)-1):
#             if L[j+1] == L[j]:
#                 run += 1
#             else:
#                 i = j + 1
#                 break
#         else:
#             i += 1
#         
#         if longest_run < run:
#             longest_run = run
#     return longest_run
#==============================================================================
    

#L1 = [1,2,3,4,4,4,4,5,6,6,6,7,7,7,7,7,7,8]
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))