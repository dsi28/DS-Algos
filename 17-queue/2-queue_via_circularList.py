# implement a queue using a circular list

class QueueCL:
    def __init__(self,maxSize):
        self.start = -1
        self.last = -1
        self.c_list = maxSize * [None]
        self.max_size = maxSize

    def __str__(self):
        if self.isEmpty():
            return 'queue is empty'
        values = [str(item) for item in self.c_list]
        return '-'.join(values) + f' start={self.start}  last={self.last}'
    
    def isFull(self):
        if self.start == 0 and self.last == self.max_size - 1:
            return True
        elif self.last + 1 == self.start:
            return True
        return False
    
    def isEmpty(self):
        if self.last == -1:
            return True
        return False
    
    def enqueue(self, value):
        if self.isFull():
            return None
        if self.start == -1 and self.last == -1:
            self.start = self.last = 0
        elif self.last + 1 == self.max_size:
            self.last = 0 
        else:
            self.last += 1
        self.c_list[self.last] = value
        return self.last
    
    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.c_list[self.start]
        new_start = 0
        if self.start == self.last:
            new_start = self.last = -1
        elif self.start + 1 == self.max_size:
            new_start = 0 
        else:
            new_start = self.start + 1
        self.c_list[self.start] = None
        self.start = new_start
        return temp
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.c_list[self.start]


    def delete(self):
        self.c_list = self.max_size * [None]
        self.start = -1
        self.last = -1


test = QueueCL(maxSize=3)
result = test.enqueue(1)
result = test.enqueue(2)
result = test.enqueue(3)
result = test.enqueue(3)
print(result)
print(test)
result = test.dequeue()
result = test.dequeue()
print(result)
print(test)
result = test.enqueue(4)
print(result)
print(test)
result = test.enqueue(5)
print(result)
print(test)
result = test.peek()
print(result)
test.dequeue()
print(test)
test.enqueue(12)
print(test)
test.delete()
print(test)