# create the class and methods for a queue made with python list

class QueueList:
    def __init__(self):
        self.queue_list = []
    
    def __str__(self):
        if self.isEmpty():
            return 'list is empty'
        result = "Front "
        for item in self.queue_list:
            result += f"- {item} "
        return result
    
    def isEmpty(self):
        if len(self.queue_list) == 0:
            return True
        return False
    
    def enqueue(self,value):
        self.queue_list.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue_list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.queue_list[0]
    
    def delete(self):
        self.queue_list = []


test = QueueList()
test.enqueue(22)
test.enqueue(32)
test.enqueue(77)
test.enqueue(11)

print(test)
test.dequeue()
test.dequeue()
print(test)
test.peek()
test.dequeue()
test.dequeue()
print(test)
test.enqueue(2)
print(test)
test.delete()
print(test)