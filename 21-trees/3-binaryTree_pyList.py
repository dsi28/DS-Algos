# implment a binary tree with a python list


class BinaryTreeList:
# constructor for binary tree list
    # tc: O(1)
    # sc: O(n) due to creation of list with n elements
    def __init__(self, size):
        self.t_list = size * [None]
        self.size = size
        self.lastUsedIndex = 0

    def isFull(self):
        if self.lastUsedIndex + 1 == self.size:
            return True
        return False

    # Insert item at next availible index
        # tc: O(1)
        # sc: O(1)
    def insert(self,new_value):
        if self.isFull():
            return 'list is full'
        self.t_list[self.lastUsedIndex + 1] = new_value
        self.lastUsedIndex += 1
        return f'{new_value} was inserted'
    
    # searchValue. search for value in list using for loop
        # tc: O(n)
        # sc: O(1)
    def searchValue(self,target_value):
        for i in range(1, self.size):
            if self.t_list[i] == target_value:
                return f'found {target_value} at index {i}'
        return f'{target_value} not found'
    
    # preorder traversal of python list 
        # tc: O(n)
        # sc: O(n)
    def preOrderTraversal(self, index_x=1):
        if index_x > self.lastUsedIndex:
            return
        print(self.t_list[index_x])
        self.preOrderTraversal(index_x * 2) # left node
        self.preOrderTraversal((index_x * 2) + 1) # right node

    # in order traversal
        # tc:O(n)
        # sc: O(n)
    def inOrderTraversal(self, index_x=1):
        if index_x > self.lastUsedIndex:
            return
        self.inOrderTraversal(index_x * 2)
        print(self.t_list[index_x])
        self.inOrderTraversal((index_x * 2) + 1)

    # post order traversal
        # tc: O(n)
        # sc: O(n)
    def postOrderTraversal(self, index_x=1):
        if index_x > self.lastUsedIndex:
            return
        self.postOrderTraversal(index_x * 2)
        self.postOrderTraversal((index_x * 2) + 1)
        print(self.t_list[index_x])

    # level order traversal. for loop
        # tc: O(n)
        # sc: O(1)
    def levelOrderTraversal(self):
        for i in range(1, self.lastUsedIndex + 1):
            print(self.t_list[i])

    # delete node with target valuel
        # tc: O(n)
        # sc: O(1)
    def deleteNode(self, target_value):
        if self.lastUsedIndex == 0:
            return 'tree is empty'
        for i in range(1, self.lastUsedIndex + 1):
            if self.t_list[i] == target_value:
                self.t_list[i] = self.t_list[self.lastUsedIndex]
                self.t_list[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return f'deleted value {target_value} at index {i}'
    
    # delete tree
        # tc: O(1)
        # sc: O(1)
    def deleteTree(self):
        self.t_list = None
        self.lastUsedIndex = 0
        return 'tree deleted'


list_tree = BinaryTreeList(7)
list_tree.insert(1)
list_tree.insert(2)
list_tree.insert(3)
list_tree.insert(4)
list_tree.insert(5)
list_tree.insert(6)
list_tree.insert(7)
print(list_tree.t_list)
result = list_tree.searchValue(7)
print(result)
print('pre order traversal: ')
list_tree.preOrderTraversal()
print('xxxxxxxxx')
print('in order traversal:')
list_tree.inOrderTraversal()
print('xxxxxxxxx')
print('post order traversal')
list_tree.postOrderTraversal()
print('xxxxxxxxx')
print('level order traversal:')
list_tree.levelOrderTraversal()
print('xxxxxxxxxx')
result = list_tree.deleteNode(3)
print(result)
list_tree.levelOrderTraversal()
print('xxxxxxxxxx')
result = list_tree.deleteTree()
print(result)
list_tree.levelOrderTraversal()