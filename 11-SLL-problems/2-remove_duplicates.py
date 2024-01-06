# Remove Duplicates
# Given the head of a sorted linked list, delete all 
# duplicates such that each element appears only once. 
# Return the linked list sorted as well. 
# Example 1:
#     Input: head = [1,1,2]
#     Output: [1,2]
# Example 2:
#     Input: head = [1,1,2,3,3]
#     Output: [1,2,3]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# TC: O(n)  - keeping in mind this could be O(n^2) if set look up operation is worst case O(n)
# SC: O(n)  
class Solution(object):
    def deleteDuplicates(self, head):
        values_set = set()
        values_set.add(head.val)
        cur = head.next
        prev = head
        while cur != None:
            if cur.val in values_set:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                values_set.add(cur.val)
                cur = cur.next
                prev = prev.next
        return head