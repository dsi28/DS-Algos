from linkedList import LinkedList, Node

def seperate(ll, x):
    temp_x = Node(value=x)
    temp_x.next = ll.head
    prev_x = None
    ll.head = temp_x
    cur = ll.head
    while cur is not None and cur.next is not None:
        next_t = cur.next
        if next_t.value < x:
            temp = next_t.next
            next_t.next = ll.head
            ll.head = next_t
            cur.next = temp
            if prev_x is None:
                prev_x = next_t
            # do not increment cur
        elif cur.next.value > x:
            cur = cur.next
        else: # cur.value = x
            cur_next_temp = cur.next.next
            temp_x_next_temp = temp_x.next
            temp_x.next = cur.next
            cur.next.next = temp_x_next_temp
            cur.next = cur_next_temp
    prev_x.next = temp_x.next
    temp_x.next = None


        
test = LinkedList()
test.generate(20,1,8)
print(test)
seperate(test, 5)
print(test)

