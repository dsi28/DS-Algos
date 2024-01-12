
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.value}"
    
class LinkedList:
    def __init__(self,value=None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur
            cur = cur.next
    
    def __str__(self):
        result = [f"{i.value}" for i in self]
        return ' -> '.join(result)
    
    def __len__(self):
        length_1 = 0
        cur = self.head
        while cur is not None:
            length_1 += 1
            cur = cur.next
        return length_1
    
    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail
    
    def generate(self, n, min_val, max_val):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min_val,max_val))
        return self
    
# test_LL = LinkedList()
# test_LL.generate(12,2,77)
# print(test_LL)
# print(len(test_LL))

        