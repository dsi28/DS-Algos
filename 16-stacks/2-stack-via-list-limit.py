# stack using a python list.
# with  size limit

class StackLimit:
    def __init__(self,limit):
        self.max_size = limit
        self.s_list = []

    def __str__(self):
        if self.isEmpty():
            return 'stack is empty'
        values = list(reversed(self.s_list))
        values = [str(item) for item in values]
        return '<-'.join(values)
    
    def isEmpty(self):
        if self.s_list == [] or self.s_list == None:
            return True
        return False
    
    def isFull(self):
        if len(self.s_list) == self.max_size:
            return True
        return False
    
    def push(self,value):
        if self.isFull():
            return None
        self.s_list.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.s_list.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.s_list[len(self.s_list) - 1]
    
    def delete(self):
        self.s_list = None
        self.max_size = None


test = StackLimit(4)
test.push(12)
test.push(13)
test.push(14)
test.push(15)
test.push(16)
print(test.pop())
print(test)
print(test.peek())
test.delete()
print(test)