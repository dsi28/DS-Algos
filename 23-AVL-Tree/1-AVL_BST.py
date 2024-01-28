#  implelment AVL Tree using linked list

from queue import Queue


class AVLTree:
    def __init__(self, value=None):
        self.data = value
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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
        return 'empty?'
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


def getHeight(root_node):
    if root_node is None:
        return 0
    return root_node.height

# tc: O(1), sc: O(1)
def rightRotation(disBalancedNode):
    new_root = disBalancedNode.leftChild
    disBalancedNode.leftChild = disBalancedNode.leftChild.rightChild
    new_root.rightChild = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.leftChild), getHeight(disBalancedNode.rightChild))
    new_root.height = 1 + max(getHeight(new_root.leftChild), getHeight(new_root.rightChild))
    return new_root

# tc: O(1), sc: O(1)
def leftRotation(disBalancedNode):
    new_root = disBalancedNode.rightChild
    disBalancedNode.rightChild = disBalancedNode.rightChild.leftChild
    new_root.leftChild = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.leftChild), getHeight(disBalancedNode.rightChild))
    new_root.height = 1 + max(getHeight(new_root.leftChild), getHeight(new_root.rightChild))
    return new_root    


def getBalance(root_node):
    if root_node is None:
        return 0
    return getHeight(root_node.leftChild) - getHeight(root_node.rightChild)

# tc: O(logN), sc: O(logN)
#  this is because recursion is only done on one side of the tree
def insertNode(cur, new_value):
    # insert node
    if cur is None:
        return AVLTree(new_value)
    if cur.data > new_value:
        cur.leftChild = insertNode(cur.leftChild, new_value)
    else:
        cur.rightChild = insertNode(cur.rightChild, new_value)

    # update height
    cur.height = 1 + max(getHeight(cur.leftChild), getHeight(cur.rightChild))

    # check balance
    balance = getBalance(cur)
    
    # Left left (LL) condition
    if balance > 1 and cur.leftChild.data > new_value:
        return rightRotation(cur)
    # Left right (LR) condition
    if balance > 1 and cur.leftChild.data < new_value:
        cur.left = leftRotation(cur.leftChild)
        return rightRotation(cur)
    # right right (RR) condition
    if balance < -1 and cur.rightChild.data < new_value:
        return leftRotation(cur)
    # right left (RL) condition
    if balance < -1 and cur.rightChild.data > new_value:
        cur.rightChild = rightRotation(cur.rightChild)
        return leftRotation(cur)
    return cur

def getMinNode(cur):
    if cur is None or cur.leftChild is None:
        return cur
    return getMinNode(cur.leftChild)

# tc: O(logN), sc: O(logN)
def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    
    return rootNode
                

testAVL = AVLTree(5)
testAVL = insertNode(testAVL, 10)
testAVL = insertNode(testAVL, 15)
testAVL = insertNode(testAVL, 20)
testAVL = deleteNode(testAVL, 15)
result = levelOrderTraversal(testAVL)
print(result)