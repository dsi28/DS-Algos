#  implement stack using python list..
#  no size limit

class Stack:
    def __init__(self):
        self.s_list = []

    def __str__(self):
        if self.isEmpty():
            return 'stack empty'
        values = list(reversed(self.s_list))
        values = [str(item) for item in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.s_list == [] or self.s_list == None:
            return True
        return False
    
    def push(self, value):
        self.s_list.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else: 
            pop_element = self.s_list.pop()
            return pop_element
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.s_list[len(self.s_list) - 1]
    
    def delete(self):
        self.s_list = None



test = Stack()
test.push(1)
test.push(2)
test.push(3)
print(test)
print(test.pop())
print('iiii')
print(test)
print(test.peek())
test.delete()
print(test)