# Remove Linked List Elements
# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has 
# Node.val == val, and return the new head.

# Example 1:
#     Input: head = [1,2,6,3,4,5,6], val = 6
#     Output: [1,2,3,4,5]

# Example 2:
#     Input: head = [], val = 1
#     Output: []

# Example 3:
#     Input: head = [7,7,7,7], val = 7
#     Output: []




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC: O(n)
# SC: O(1)
class Solution(object):
    def removeElements(self, head, val):
        # When we find one element that is not val set head
        cur = head
        prev = head 
        
        while cur != None:
            if cur.val == val:
                if cur == head:
                    head = cur.next
                    cur = cur.next
                    prev = prev.next
                else:
                    prev.next = cur.next
                    cur.next = None
                    cur = prev.next
            else:
                if cur == head:
                    head = cur
                prev = cur    
                cur = cur.next
        return head