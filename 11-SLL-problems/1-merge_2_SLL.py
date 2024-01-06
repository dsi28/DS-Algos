# Merge Two Sorted Linked List
# You are given the heads of two sorted linked lists list1 and list2. 
# Merge the two lists in a one sorted list. The list should be made by 
# splicing together the nodes of the first two lists.
# Return the head of the merged linked list.   
# Example 1: 
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
# Example 3: 
# Input: list1 = [], list2 = [0]
# Output: [0] 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # TC: O(n+m)
    # SC: O(1) 
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 == None and l2 == None:
            return l1
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
            
        # compare heads to see which one goes first
        if l1.val > l2.val:
           l1,l2 = l2,l1
        head_1 = l1
        while l1 != None:
            if l2 == None:
                return head_1
            if l1.next.val > l2.val:
                temp_l1 = l1.next
                temp_l2 = l2
                l1.next = temp_l2 
                l2 = l2.next
                temp_l2.next = temp_l1
            if l1.next.next == None and l2 != None:
                l1.next.next = l2
                return head_1
            else:
                l1 = l1.next
        return head_1
    def improved_mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return_head = ListNode(-1)
        prev = return_head

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        if l1 == None:
            prev.next = l2
        else:
            prev.next = l1