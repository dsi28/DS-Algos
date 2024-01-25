# binary tree implementation with linked lists
from queueViaList import QueueList

class TreeNode:

    # constructor. 
    # TC: O(1)
    # SC: O(1)
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# pre order traversal 
# tc: O(n)
# sc: O(n) due to stack accumulation because of recursion 
def preOrderTraversal(root_node):
    if root_node is None:
        return 
    print(root_node.data)
    preOrderTraversal(root_node.leftChild)
    preOrderTraversal(root_node.rightChild)

# in order traversal
    # tc: O(n)
    # sc: O(n)
def inOrderTraversal(root_node):
    if root_node is None:
        return 
    inOrderTraversal(root_node.leftChild)
    print(root_node.data)
    inOrderTraversal(root_node.rightChild)

# post order traversal
    # tc: O(n)
    # sc: O(n)
def postOrderTraversal(root_node):
    if root_node is None:
        return
    postOrderTraversal(root_node.leftChild)
    postOrderTraversal(root_node.rightChild)
    print(root_node.data)

# level order traversal
    # tc: O(n)
    # sc: O(n) due to the creation of the queue
def levelOrderTraversal(root_node):
    if root_node is None:
        return
    track_queue = QueueList()
    track_queue.enqueue(root_node)
    while not track_queue.isEmpty():
        root = track_queue.dequeue()
        print(root.data)
        if root.leftChild is not None:
            track_queue.enqueue(root.leftChild)
        if root.rightChild is not None:
            track_queue.enqueue(root.rightChild)

# search using level order traversal:
    # tc: O(n)
    # sc: O(n)
def searchInOrderT(root_node,target_value):
    if root_node is None:
        return 'empty'
    track_queue = QueueList()
    track_queue.enqueue(root_node)
    while not (track_queue.isEmpty()):
        root = track_queue.dequeue()
        if root.data == target_value:
            return 'Found!'
        if root.leftChild is not None:
            track_queue.enqueue(root.leftChild)
        if root.rightChild is not None:
            track_queue.enqueue(root.rightChild)
    return 'Not found'

def insertLevelOrder(root_node, new_node):
    if root_node is None:
        return
    track_queue = QueueList()
    track_queue.enqueue(root_node)
    while not (track_queue.isEmpty()):
        root = track_queue.dequeue()
        if root.leftChild is not None:
            track_queue.enqueue(root.leftChild)
        else:
            root.leftChild = new_node
            return 'inserted left child'
        if root.rightChild is not None:
            track_queue.enqueue(root.rightChild)
        else:
            root.rightChild = new_node
            return 'inserted right child'


def getDeepestNode(root_node):
    if root_node is None:
        return 'empty'
    track_queue = QueueList()
    track_queue.enqueue(root_node)
    root = root_node
    while not (track_queue.isEmpty()):
        root = track_queue.dequeue()
        if root.leftChild is not None:
            track_queue.enqueue(root.leftChild)
        if root.rightChild is not None:
            track_queue.enqueue(root.rightChild)
    return root


def deleteDeepestNode(root_node, deepest_Node):
    if root_node is None:
        return 'empty'
    track_queue = QueueList()
    track_queue.enqueue(root_node)
    while not (track_queue.isEmpty()):
        root = track_queue.dequeue()
        if root.data is deepest_Node:
            root.data = None
            root = None
            return 
        if root.leftChild is not None:
            if root.leftChild.data is deepestNode:
                root.leftChild = None
                return
            else:
                track_queue.enqueue(root.leftChild)
        if root.rightChild is not None:
            if root.rightChild.data is deepestNode:
                root.rightChild = None
                return
            else:
                track_queue.enqueue(root.rightChild)

# delete node
# calls getdeepestnode and delete deepestnode functions
    # tc: O(n)
    # sc: O(n)
def deleteNode(root_node,target_value):
    if root_node is None:
        return 
    track_queue = QueueList()
    track_queue.enqueue(root_node)
    while not (track_queue.isEmpty()):
        root = track_queue.dequeue()
        if root.data == target_value:
            deepest_node = getDeepestNode(root_node)
            root.data = deepest_node.data
            deleteDeepestNode(root_node,deepest_node)
            return 'node deleted'
        if root.leftChild is not None:
            track_queue.enqueue(root.leftChild)
        if root.rightChild is not None:
            track_queue.enqueue(root.rightChild)
    return 'target node not deleted'

# delete tree
    # tc: O(1)
    # sc: O(1)
def deleteTree(root_node):
    root_node.leftChild = None 
    root_node.rightChild = None
    root_node.data = None
    return "deleted tree"

tree = TreeNode('Pangea')
tree.leftChild = TreeNode('Americas')
tree.rightChild = TreeNode('Eurasia')
tree.leftChild.leftChild = TreeNode('north america')
tree.leftChild.rightChild = TreeNode('south america')

print('preOrder traversal:')
preOrderTraversal(tree)
print('///////\ninOrder traversal:')
inOrderTraversal(tree)
print('////////\npostOrder traversal:')
postOrderTraversal(tree)
print('//////////\nlevelOrder traversal:')
levelOrderTraversal(tree)
print('////////')
result = searchInOrderT(tree, 'america')
print(result)
print('///////////insert ')
result = insertLevelOrder(tree, TreeNode('europe'))
result = insertLevelOrder(tree, TreeNode('asia'))

print('result: ',result)
levelOrderTraversal(tree)
print('/////\ndeepest Node: ')
deepestNode = getDeepestNode(tree)
print(deepestNode)
print('delete deepest node')
deleteDeepestNode(tree,deepestNode)
levelOrderTraversal(tree)
print('full delete test:')
result = deleteNode(tree, 'Americas')
print('result: ',result)
levelOrderTraversal(tree)
print(' delete tree: ')
deleteTree(tree)
levelOrderTraversal(tree)