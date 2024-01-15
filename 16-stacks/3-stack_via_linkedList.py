# create stack using linked list
# 

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    def __str__(self):
        return self.value
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next
    
class StackLL:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return "stack is empty"
        values = [str(item) for item in self.linkedList]
        return 'top ' + '\n'.join(values) + ' end'

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.linkedList.head
        self.linkedList.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        temp = self.linkedList.head
        self.linkedList.head = temp.next
        temp.next = None
        return temp

    def peek(self):
        if self.isEmpty():
            return None
        return self.linkedList.head 

    def delete(self):
        self.linkedList.head = None


test = StackLL()
test.push(22)
test.push(33)
test.push(44)
test.push(55)
print(test)  
test.pop()
test.pop()
test.pop()
result = test.pop()
print(result.value)
test.push(77)
print(test)
test.delete()
print(test)