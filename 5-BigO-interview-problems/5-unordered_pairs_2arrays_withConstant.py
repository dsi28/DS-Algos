# find the tc

# O(ab) # this is not O(abc) becuase the third loop has a constant 
#       range there for even though its still a loop its counts as O(1).

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))