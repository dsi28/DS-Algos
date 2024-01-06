

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # tc: O(n)
    # sc: O(1) 
    def reverseList(self, head):
        cur = head
        if cur == None:
            return head
        while cur.next != None:
            temp = cur.next
            cur.next = temp.next
            temp.next = head
            head = temp
        return head