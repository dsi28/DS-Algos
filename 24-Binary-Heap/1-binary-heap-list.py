# binary heap implmentation using python list

class Heap:

    # tc: O(1), sc: O(n) due to None array creation
    def __init__(self, size):
        self.maxSize = size - 1
        self.curSize = 0 
        self.heapList = size * [None]

    def peek(self):
        if self.heapList is None or self.heapList[1] is None:
            return 'root not set'
        return self.heapList[1]
    
    def getSize(self):
        return self.curSize
    
    def levelOrderTraversal(self):
        if self.heapList is None:
            return None
        result = "top - "
        for i in range(1, self.curSize + 1):
            result += str(self.heapList[i]) + " - "
        print(result + " last")

    # tc: O(logN), sc: O(logN)
    def heapValidCheck(self, childIndex, heapType):
        parentIndex = int(childIndex//2)
        print(parentIndex)
        if parentIndex  < 1:
            return
        if heapType == "min":
            if self.heapList[childIndex] < self.heapList[parentIndex]:
                temp = self.heapList[childIndex]
                self.heapList[childIndex] = self.heapList[parentIndex]
                self.heapList[parentIndex] = temp
            self.heapValidCheck(parentIndex, 'min')
        elif heapType == "max":
            if self.heapList[childIndex] > self.heapList[parentIndex]:
                temp = self.heapList[childIndex]
                self.heapList[childIndex] = self.heapList[parentIndex]
                self.heapList[parentIndex] = temp
            self.heapValidCheck(parentIndex, 'max')
    
    # tc: O(logN), sc: O(logN)
    def heapInsert(self, newValue, heapType):
        if self.curSize + 1 > self.maxSize:
            return 'heap is empty'
        self.heapList[self.curSize + 1] = newValue
        self.curSize += 1
        self.heapValidCheck(self.curSize, heapType)
        print(self.heapList)
        return f"{newValue} has been added"
     
heapTest = Heap(5)
heapTest.heapInsert(4, 'max')
heapTest.heapInsert(5, 'max')
heapTest.heapInsert(2, 'max')
heapTest.heapInsert(1, 'max')
heapTest.heapInsert(7, 'max')
heapTest.levelOrderTraversal()
