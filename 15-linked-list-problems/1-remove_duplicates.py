# Remove Duplicates
# Write a function to remove duplicates from an unsorted linked list. 
# Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 
# Output 1 -> 2 -> 3 -> 4 -> 5 

from linkedList import LinkedList

def remove_duplicates(ll):
    if ll.head is None:
        return None
    cur = ll.head
    track_ll = set([cur.value])
    while cur is not None and cur.next is not None:
        if cur.next.value in track_ll:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = None # do not move cur = cur.next becuase we got rid of cur.next so there is a new cur.next that has to be checked
        else:
            track_ll.add(cur.next.value)
            cur = cur.next
    return ll


test = LinkedList()
test.generate(7,1,3)
print(test)
result = remove_duplicates(test)
print(result)