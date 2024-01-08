
class NodeItem:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLL:
    # constructor with one node
    # tc: O(1)
    # sc: O(1)
    def __init__(self, value):
        new_node = NodeItem(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1


    # constructor of empty CLL 
    # tc: O(1)
    # sc: O(1)
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
    
    # print functionality
    # tc: O(n)
    # sc: O(1)
    def __str__(self):
        cur = self.head
        temp = ""
        for _ in range(self.length):
            if cur != self.tail:
                temp += f"{cur.value} -> "
            else: temp += f"{cur.value}"
            cur = cur.next
        return temp
    
    #  insert at the end of list
    #  tc: O(1)
    #  sc: O(1)
    def append(self, value):
        new_node = NodeItem(value)
        if self.head: # or use self.length > 0 
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        self.length += 1 

    # insert node at the begining of the list
    # tc: O(1)
    # sc: O(1)
    def prepend(self, value):
        new_node = NodeItem(value)
        if self.head is not None:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node  
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        self.length += 1

    
    # insert at given index
    # tc: O(n)
    # sc: O(1)
    def insert(self,value,location):
        new_node = NodeItem(value)
        if (location > (self.length)) or location < 0:
            return False
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif location == 0:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        else:
            prev = self.head
            for _ in range(0, location - 1):
                prev = prev.next
            if prev == self.tail:
                new_node.next = self.head
                self.tail.next = new_node
                self.tail = new_node
            else:
                new_node.next = prev.next
                prev.next = new_node
        self.length += 1


test = CircularLL(22)
print(test)
test.append(11)
test.append(44)
print(test)
test.prepend(0)
test.prepend(99)
print(test)
test.insert("a",5)
print(test)