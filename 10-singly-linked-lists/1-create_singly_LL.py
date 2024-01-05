# Create Simple Singly Linked List DS
# Write a code in the language of your choice to implement a singly linked list.
# A singly linked list has the following properties:
# -Each node contains a piece of data. 
# Node class constructor  takes a value as an argument and 
# initializes the value attribute of the node.
# -Each node also holds a reference (or link) to the next 
# node in the list. A  next attribute, initialized to None, 
# which will store a reference to the next node in the list.
# -LinkedList class constructor  takes a value as an argument and 
# creates new node object based on Node class with that value.
# -head and tail attributes of the linked list to point to the new node.
# -A length attribute, initialized to 1, which represents the current number
# of nodes in the list.

# TC: O(1)
# SC: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# TC: O(1)
# SC: O(1)
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Write a function to insert a new element at the beginning of a singly linked list.
        # TC: O(1)
        # SC: O(1) 
    def insert_front(self, value):
        new_node = Node(value)
        if self.head == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Write a method to insert a new element at the end of a singly linked list.
        # TC: O(1)
        # SC: O(1)
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def remove(self, t_index):
        if t_index > self.length or t_index < 0 or self.head == None:
            return None
        elif t_index == 0:
            if self.head == self.tail:
                self.tail = None
            current_node = self.head
            self.head = current_node.next
            current_node.next = None
            self.length -= 1
            return current_node
        # elif t_index == self.length - 1:
        #     current_node = self.head
        #     while current_node.next != self.tail:
        #         current_node = current_node.next
        #     temp = current_node.next
        #     current_node.next = None
        #     self.tail = current_node
        #     self.length -=1
        #     return temp
        else:
            current_node = self.head
            for _ in range(t_index - 1):#range(0, t_index - 1):
                current_node = current_node.next
            temp = current_node.next
            if temp == self.tail:
                self.tail = current_node    
            current_node.next = current_node.next.next
            temp.next = None
            self.length -= 1
            return temp




