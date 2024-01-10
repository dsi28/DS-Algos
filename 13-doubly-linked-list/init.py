
class Node:
    # tc: O(1)
    # sc: O(1)
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.value}"


class DLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        cur = self.head
        result = ""
        while cur is not None:
            result += f"{cur.value}"
            if cur != self.tail:
                result += ' <-> '
            cur = cur.next
        return result

    # add node to end of doubly linked list
    # Tc: O(1)
    # sc: O(1)
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    # add node to front of list
    # tc: O(1)
    # sc: O(1) 
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.length += 1
    
    # print value of every node
    # tc: O(n)
    # sc: O(1)
    def traverse(self):
        cur = self.head
        while cur is not None:
            print(f"{cur.value}")
            cur = cur.next

    # print values of every node from tail to head
    # tc: O(n)
    # sc: O(1)
    def reverse_traverse(self):
        cur = self.tail
        while cur is not None:
            print(cur.value)
            cur = cur.prev

    # search for node given a value
    # tc: O(n)
    # sc: O(1)
    def search(self,target_value):
        start = self.head
        end = self.tail
        while start != end and end.next != start:
            if start.value == target_value:
                return True
            elif end.value == target_value:
                return True
            start = start.next
            end = end.prev
        if start.value == target_value:
            return True
        else: return False

    def get(self, target_index):
        if target_index >= self.length or target_index < 0 or self.length == 0:
            return None
        elif target_index <= self.length // 2:
            cur = self.head
            for _ in range(target_index):
                cur = cur.next
            return cur
        else:
            cur = self.tail
            for _ in range(self.length - 1, target_index, -1):
                cur = cur.prev
            return cur

        



node_test = Node(33)
print(node_test)
doub_ll = DLinkedList(22)
doub_ll.append(77)
doub_ll.append(44)
print(doub_ll)
doub_ll.prepend(51)
doub_ll.prepend(33)
print(doub_ll)
doub_ll.traverse()
print(doub_ll)
doub_ll.reverse_traverse()
result = doub_ll.search(31)
print(result)
result = doub_ll.get(3)
print(result)