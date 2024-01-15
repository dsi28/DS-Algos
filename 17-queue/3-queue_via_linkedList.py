# implement queue with linked list

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    def __str__(self):
        cur = self.head
        result = "head:"
        while cur is not None:
            result += f' {cur.value} - '
            cur = cur.next
        return result
    
class QueueLL:
    def __init__(self):
        self.ll_queue = LinkedList()
    
    def __str__(self):
        return self.ll_queue.__str__()
    
    def isEmpty(self):
        if self.ll_queue.head == None:
            return True
        return False

    def enqueue(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.ll_queue.head = self.ll_queue.tail = new_node
        else:
            self.ll_queue.tail.next = new_node
            self.ll_queue.tail = new_node
    
    def dequeue(self):
        if self.isEmpty():
            return None
        temp = self.ll_queue.head
        if self.ll_queue.head == self.ll_queue.tail:
            self.ll_queue.head = self.ll_queue.tail = None
        else:
            self.ll_queue.head = self.ll_queue.head.next
        return temp
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll_queue.head
    
    def delete(self):
        self.ll_queue.head = self.ll_queue.tail = None


test = QueueLL()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
print(test)
test.dequeue()
test.dequeue()
test.dequeue()
test.dequeue()
print(test)
test.enqueue(4)
test.enqueue(5)
print(test.peek())
print(test)
test.delete()
test.enqueue(1)
print(test)