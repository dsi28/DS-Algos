# you have two numbers represented by a linked list, where each node contains a single digit. 
# the digits are stored in reverse order, such that the 1's digit is at the head of the list. 
# write a function that adds the two numbers and returns the sum as a linked list.

from linkedList import LinkedList, Node

# tc: O(n) , o(a+b)
# sc: O(1)
def sum_ll(list_1, list_2):
    cur_1 = list_1.head
    cur_2 = list_2.head
    remainder = 0
    prev_1 = list_1.head
    while cur_1 is not None:
        if cur_2 is not None:
            temp = remainder + cur_1.value + cur_2.value
            if temp > 9:
                cur_1.value = temp % 10
                remainder = int((temp - cur_1.value) / 10)
            else:
                cur_1.value += cur_2.value + remainder
                remainder = 0
            cur_2 = cur_2.next 
        print(cur_1.value , " remainder", remainder)
        prev_1 = cur_1
        cur_1 = cur_1.next

    while cur_2 is not None:
        prev_1.next = cur_2
        if cur_2.value + remainder > 9:
            remainder =+ cur_2 
        else:
            cur_2.value += remainder
            remainder = 0
        prev_1 = cur_2
        cur_2 = cur_2.next

    while remainder > 0:
        if remainder < 9:
            new_node = Node(remainder)
            remainder = 0
        else:
            new_node = Node(remainder%10)
            remainder = int((remainder - (remainder %  10)) / 10)
        prev_1.next = new_node
        prev_1 = prev_1.next


    print('remainder ',remainder)
    return list_1

# TC: O(n)
# sc: O(n)
def better_sum_ll(list_1, list_2):
    cur_1 = list_1.head
    cur_2 = list_2.head
    carry = 0
    sum_list = LinkedList()
    temp_node = Node(0)
    sum_list.head = temp_node
    cur_s = sum_list.head
    while cur_1 or cur_2:
        total = carry
        if cur_1 is not None:
            total += cur_1.value
            cur_1 = cur_1.next
        if cur_2 is not None:
            total += cur_2.value
            cur_2 = cur_2.next
        remainder = total % 10
        new_node = Node(remainder)
        cur_s.next = new_node
        cur_s = cur_s.next
        carry = int((total - remainder) / 10)
    sum_list.head = sum_list.head.next
    return sum_list


test = LinkedList()
test.generate(3,1,9)
test_2 = LinkedList()
test_2.generate(4,1,9)
print(test)
print(test_2)
result = better_sum_ll(test,test_2)
print(result)
print('seperate')
result = sum_ll(test,test_2)
print(result)
