
class NodeItem:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f'{self.value}'

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

    # traverse and print each element
        # tc: O(n)
        # sc: O(1) 
    def traverse(self):
        if self.head is None:
            print('empty list')
        cur = self.head
        while cur is not None:
            print(cur.value)
            cur = cur.next
            if cur == self.head:
                break
    
    # search for target value
    # tc: O(n)
    # sc: O(1)
    def search(self, target_value):
        cur = self.head
        while cur is not None:
            if cur.value == target_value:
                return True
            cur = cur.next
            if cur == self.head:
                break
        return False
    
    # return node at given index
    # tc: O(n)
    # sc: O(1)
    def get(self, target_index):
        cur = self.head
        count = 0
        while cur is not None:
            if count == target_index:
                return cur
            cur = cur.next
            count += 1
            if cur == self.head:
                break
        return False
    
    # update value of node at given index
    # tc: O(n)
    # sc: O(1)
    def set(self, target_value, target_index):
        update_node = self.get(target_index)
        if update_node != False:
            update_node.value = target_value
            return True
        return False      

    # pop first node in list
    # tc: O(1)
    # sc: O(1)
    def pop_first(self):
        if self.head is None:
            return None
        pop_node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.length -= 1
        pop_node.next = None
        return pop_node
    
    # remove and return last node
    # tc: O(n)
    # sc: O(1)
    def pop(self):
        if self.head is None:
            return None
        pop_node = self.tail
        if self.head == self.tail:
            self.head = None 
            self.tail = None
        else:
            cur = self.head 
            while cur.next != self.tail:
                cur = cur.next
            self.tail.next = None
            cur.next = self.head
            self.tail = cur
        self.length -= 1
        return pop_node    
    
    # remote node at given index
    # tc: O(n)
    # sc: O(1)
    def remove(self, target_index):
        if self.head is None:
            return None
        pop_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        elif target_index == 0:
            pop_node = self.pop_first()
        else:
            prev = self.get(target_index - 1) # get prev
            if prev != False and prev != self.tail:
                pop_node = prev.next
                if pop_node is self.tail:
                    self.tail = prev
                    prev.next = self.head
                else:
                    prev.next = pop_node.next
                pop_node.next = None
            else: 
                print('No')
                return None
        self.length -= 1
        return pop_node.value
    
    # delete all the nodes in the given list
    # tc: O(1)
    # sc: O(1)
    def delete_all(self):
        if self.head is not None:
            self.head = None
            self.tail.next = None
            self.tail = None 
            self.length = 0
        


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
test.traverse()
print(test.search('a'))
print(test.search('b'))
print(test.search(0))
result = test.get(0)
print(result.value)
test.set('*', 3)
print(test)
result = test.pop_first()
print('pop first ', result)
print(test)
result = test.pop()
print('pop ', result)
print(test)
print(test.length)
result = test.remove(3)
print('remove ', result)
print(test)
test.delete_all()
print(test)