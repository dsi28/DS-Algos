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
        # print(self.heapList)
        return f"{newValue} has been added"
    
    # tc: O(logN), sc: O(logN) 
    def heapExtract(self, curIndex, heapType):
        leftChildIndex = curIndex * 2
        rightChildIndex = (curIndex * 2) + 1
        swapChild = 0
        if self.curSize < curIndex: #condition where node at curIndex has no children
            return
        elif self.curSize == leftChildIndex: #condition where node at curIndex has only one child
            if heapType == 'min':
                if self.heapList[leftChildIndex] < self.heapList[curIndex]:
                    temp = self.heapList[leftChildIndex]
                    self.heapList[leftChildIndex] = self.heapList[curIndex]
                    self.heapList[curIndex] = temp
                return
            else: # heapType == 'max'
                if self.heapList[leftChildIndex] > self.heapList[curIndex]:
                    temp = self.heapList[leftChildIndex]
                    self.heapList[leftChildIndex] = self.heapList[curIndex]
                    self.heapList[curIndex] = temp
                return
        else: # node at curIndex has two children.
            if heapType == 'min': 
                # get lesser of two child indexies
                if self.heapList[leftChildIndex] < self.heapList[rightChildIndex]:
                    swapChild = leftChildIndex
                else:
                    swapChild = rightChildIndex
                # check if value at swap child is less than value at curIndex
                if self.heapList[swapChild] < self.heapList[curIndex]:
                    temp = self.heapList[swapChild]
                    self.heapList[swapChild] = self.heapList[curIndex]
                    self.heapList[curIndex] = temp
            else: # heap type is 'max'
                if self.heapList[leftChildIndex] > self.heapList[rightChildIndex]:
                    swapChild = leftChildIndex
                else:
                    swapChild = rightChildIndex
                # check if value at swapChild is greater than value at curIndex
                if self.heapList[swapChild] > self.heapList[curIndex]:
                    temp = self.heapList[swapChild]
                    self.heapList[swapChild] = self.heapList[curIndex]
                    self.heapList[curIndex] = temp
        self.heapExtract(swapChild,heapType)

    def extract(self, heapType):
        if self.curSize == 0:
            return 
        else:
            extractedNode = self.heapList[1]
            self.heapList[1] = self.heapList[self.curSize]
            self.heapList[self.curSize] = None
            self.curSize -= 1
            self.heapExtract(1, heapType)
            return extractedNode
    
    def deleteHeap(self):
        self.heapList = None

heapTest = Heap(6)
heapTest.heapInsert(4, 'max')
heapTest.heapInsert(5, 'max')
heapTest.heapInsert(2, 'max')
heapTest.heapInsert(1, 'max')
heapTest.heapInsert(7, 'max')
heapTest.levelOrderTraversal()
heapTest.extract('max')
heapTest.levelOrderTraversal()