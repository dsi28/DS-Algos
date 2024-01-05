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
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

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

    # remove node at a given index
        # TC: O(N)
        # SC: O(1) 
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

    # Write a function to reverse a singly linked list. 
    # The function should reverse the original linked list. 
        # TC: O(n)
        # SC: O(1) 
    def reverse(self):
        cur_node = self.head
        while cur_node != self.tail:
            next_node = cur_node.next
            if next_node == self.tail:
                cur_node.next = None
                self.tail = cur_node
            else:
                cur_node.next = next_node.next
            next_node.next = self.head
            self.head = next_node

    # Write a function to find and return the middle node of a singly linked list. 
    # If the list has an even number of nodes, return the second of the two middle nodes. 
        # tc: O(n)
        # sc: O(1)
    def find_middle(self):
        cur_node = self.head
        for _ in range(self.length // 2):
            cur_node = cur_node.next
        return cur_node

    #Remove Duplicates from a Singly Linked List
    #Given a singly linked list, write a function that removes all the duplicates. 
    # use this linked list .
    #Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"
    #Result Linked List - "1 -> 2 -> 4 -> 3
        #tc: O(n^2)
        # sc: O(1) 
    def remove_duplicates(self):
        track_list = []
        curr_node = self.head
        prev_node = curr_node
        track_list.append(curr_node)
        while curr_node != None:
            print(curr_node.value)
            if curr_node.value in track_list:
                print('?', curr_node.value)
                prev_node.next = curr_node.next
                curr_node.next = None
                curr_node = prev_node
                self.length -= 1
            else:
                track_list.append(curr_node.value)
            prev_node = curr_node
            curr_node = curr_node.next

test_1 = LinkedList(1)
test_1.append(2)
test_1.append(4)
test_1.append(3)
test_1.append(4)
test_1.append(2)

test_1.remove_duplicates()
print(test_1)


