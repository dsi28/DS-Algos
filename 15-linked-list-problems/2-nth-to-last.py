# return the nth to last node

from linkedList import LinkedList

# tc: O(n)
# sc: O(1) 
def nth_last_with_len(ll, n):
    print(f'n {n}')
    ll_len = len(ll)
    target_index = ll_len - n
    print(f'target {target_index}')

    if target_index < 0 or n < 0:
        return None
    cur = ll.head
    for _ in range(target_index):
        cur = cur.next
    return cur


def nth_last(ll, n):
    fast = ll.head
    slow = ll.head
    for _ in range(n):
        fast = fast.next
    while fast is not None:
        fast = fast.next
        slow = slow.next
    return slow

test = LinkedList()
test.generate(7,1,10)
print(test)
index = 7
result = nth_last_with_len(test, index)
print(f'with len {result}')
result = nth_last(test, index)
print(f'non len {result}')