# find the tc of the following function

# O(a*b) . the reason is becuase the length a does not depend on b. 
#           since they are seperate this is not O(n^2)

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]