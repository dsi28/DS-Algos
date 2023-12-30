# get the runtime complexitity of the code below:

# O(n^2)

def printUnorderedPairs(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            print(array[i] + "," + array[j])