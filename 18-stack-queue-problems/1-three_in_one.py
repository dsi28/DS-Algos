# describe how to use a single python list to implment three stacks

class ThreeInOne:
    def __init__(self):
        self.to_list = 3 * [None]
        self.start_1 = self.top_1 = 0
        self.start_2 = self.top_2 = 1
        self.start_3 = self.top_3 = 2

    def __str__(self):
        values = [str(item) for item in self.to_list]
        return ' - '.join(values)
    
    def stackEmpty(self, stackNum):
        if stackNum == 1 and self.top_1 == self.start_1:
            return True
        elif stackNum == 2 and self.top_2 == self.start_2:
            return True
        elif stackNum == 3 and self.top_3 == self.start_3:
            return True
        return False
    
    def insert(self,stackNum,value):
        if stackNum == 1:
            self.to_list.insert(self.top_1,value)
            self.start_1 += 1
            self.top_2 += 1
            self.start_2 +=1
            self.top_3 += 1
            self.start_3 += 1
        elif stackNum == 2:
            self.to_list.insert(self.top_2,value)
            self.start_2 += 1
            self.top_3 += 1
            self.start_3 += 1
        elif stackNum == 3:
            self.to_list.insert(self.top_3,value)
            self.start_3 += 1
        else: return None


    def pop_item(self,stackNum):
        if self.stackEmpty(stackNum):
            return f'{stackNum} is empty'
        if stackNum == 1:
            self.to_list.pop(self.top_1)
            self.start_1 -= 1
            self.top_2 -= 1
            self.start_2 -= 1
            self.top_3 -= 1
            self.start_3 -= 1
        elif stackNum == 2:
            self.to_list.pop(self.top_2)
            self.start_2 -= 1
            self.top_3 -= 1
            self.start_3 -= 1
        elif stackNum == 3:
            self.to_list.pop(self.top_3)
            self.start_3 -= 1
        return None
    

test = ThreeInOne()
test.insert(3,32)
test.insert(3,33)
test.insert(2,22)
test.insert(2,23)
test.insert(3,34)
test.insert(2,24)
test.insert(2,25)
test.insert(1,12)
test.insert(1,13)
test.insert(3,35)
test.insert(1,14)
test.insert(1,15)
print(test)
test.pop_item(1)
test.pop_item(2)
test.pop_item(3)
test.pop_item(2)
test.pop_item(3)
test.pop_item(1)
test.pop_item(2)
test.pop_item(2)
print(test)
test.pop_item(2)
test.pop_item(2)
print(test)
    

        



    