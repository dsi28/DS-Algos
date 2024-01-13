# given two singly linked list, determine if the two lists intersect. 
# return the intersecting node. note that the  intersection is defined by reference, not value. 
# that is the if the kth node of the first list is the exact same node (by reference) 
# of the jth node in the second linked list then they are intersecting.

from linkedList import LinkedList, Node

# tc: O(n)
# sc: O(1)
def find_inter_node(list_1, list_2):
    track = set()
    cur_1 = list_1.head
    cur_2 = list_2.head
    while cur_1 or cur_2:
        if cur_1 is not None:
            # print('1', cur_1, cur_1.value)
            if cur_1 not in track:
                track.add(cur_1)
                cur_1 = cur_1.next
            else: return cur_1
        if cur_2 is not None:
            # print('2', cur_2, cur_2.value)
            if cur_2 not in track:
                track.add(cur_2)
                cur_2 = cur_2.next
            else: return cur_2
    return None


test = LinkedList()
test.generate(5,1, 9)
test_2 = LinkedList()
test_2.generate(10, 1,9)
appendList = LinkedList()
appendList.generate(3,1,5)
test.tail.next = appendList.head
test_2.tail.next = appendList.head
test_not = LinkedList()
test_not.generate(10, 1,9)


print(test)
print(test_2)
print('inter ', appendList.head)
result = find_inter_node(test, test_2)
print('result:')
print(result)