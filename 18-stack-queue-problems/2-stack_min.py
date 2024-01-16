# create implment a stack where pop, push and min() are all in tc: O(1)





# implment using linked list. as part of stack class have a self.min linked list.
# add item to self.min linked list on ever push(). 
# if new item is less than min.head insert new item to self.min
# if new item is greater than min.head insert cur min again into self.min
# this way you have the cur min at every step.
# when you pop() you should pop self.min.head   