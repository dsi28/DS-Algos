# implement binary search tree with linked list


from queue import Queue

class BinaryTreeNode:
    def __init__(self, value=None):
        self.data = value
        self.leftChild = None
        self.rightChild = None
    
    def deleteBST(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None
        return 'BST deleted'

# insert node
    # tc: O(logN)
    # sc: O(logN)
def insertNode(root_node, new_value):
    if root_node.data is None:
        root_node.data = new_value
    if root_node.data > new_value:
        if root_node.leftChild is None:
            root_node.leftChild = BinaryTreeNode(new_value)
        else:
            insertNode(root_node.leftChild, new_value)
    else:
        if root_node.rightChild is None:
            root_node.rightChild = BinaryTreeNode(new_value)
        else:
            insertNode(root_node.rightChild, new_value)
    
# pre order traversal a BST (root,left,right)
    # tc: O(n)
    # sc: O(n)
def preOrderTraversal(root_node):
    if root_node is None:
        return
    print(root_node.data)
    preOrderTraversal(root_node.leftChild)
    preOrderTraversal(root_node.rightChild)


# in orderTraversal: (left,root,right)
    # tc: O(n)
    # sc: O(n)
def inOrderTraversal(root_node):
    if root_node is None:
        return
    inOrderTraversal(root_node.leftChild)
    print(root_node.data)  
    inOrderTraversal(root_node.rightChild)  

# post orderTraversal: (left,right,root)
    # tc: O(n)
    # sc: O(n)
def postOrderTraversal(root_node):
    if root_node is None:
        return
    postOrderTraversal(root_node.leftChild)
    postOrderTraversal(root_node.rightChild) 
    print(root_node.data)  

# level order traversal with the queue module 
    # tc: O(n)
    # sc: O(n)
def levelOrderTraversal(root_node):
    if root_node is None:
        return
    track_queue = Queue()
    root = root_node
    track_queue.put(root)
    while track_queue.qsize() > 0:
        root = track_queue.get()
        print(root.data)
        if root.leftChild is not None:
            track_queue.put(root.leftChild)
        if root.rightChild is not None:
            track_queue.put(root.rightChild)

# search for target value in tree
    # tc: O(logN)
    # sc: O(logN)
def searchValue(root_node, target_value):
    if root_node is None:
        return 'tree is empty or not found'
    if root_node.data == target_value:
        return f'found {target_value}'
    elif root_node.data > target_value:
        return searchValue(root_node.leftChild, target_value)
    else:
        return searchValue(root_node.rightChild, target_value)   
        
# find min node to use as a successor?
def findMinNode(root_node):
    cur = root_node
    while cur.leftChild is not None:
        cur = cur.leftChild
    return cur

# delete node of target node. replace it with the successor if needed.
    # tc: O(logN)
    # sc: O(logN)
def deleteBSTNode(cur, target_value):
    if cur is None:
        return cur
    if cur.data > target_value:
        cur.leftChild = deleteBSTNode(cur.leftChild,target_value)
    elif cur.data < target_value:
        cur.rightChild = deleteBSTNode(cur.rightChild,target_value)
    else:
        if cur.leftChild is None:
            temp = cur.rightChild
            cur = None
            return temp
        
        if cur.rightChild is None:
            temp = cur.leftChild
            cur = None
            return temp
        
        temp = findMinNode(cur.rightChild)
        cur.data = temp.data
        cur.rightChild = deleteBSTNode(cur.rightChild, temp.data)
    return cur



bst_node = BinaryTreeNode(70)
insertNode(bst_node, 50)
insertNode(bst_node, 90)
insertNode(bst_node,60)
insertNode(bst_node,30)
insertNode(bst_node, 80)
insertNode(bst_node,100)
print('pre order traversal:')
preOrderTraversal(bst_node)
print('...........')
print('in order traversal:')
inOrderTraversal(bst_node)
print('...........')
print('post order traversal:')
postOrderTraversal(bst_node)
print('...........')
print('level order traversal:')
levelOrderTraversal(bst_node)
print('...........\nSearch')
result = searchValue(bst_node, 100)
print(result)
print('...........\nDelete')
result = deleteBSTNode(bst_node, 30)
print('result: ',result.data)
levelOrderTraversal(bst_node)