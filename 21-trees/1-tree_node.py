#  create a simple tree using the tree node class

class TreeNode:
    def __init__(self, value, children=[]):
        self.data = value
        self.children = children

    def __str__(self, level=0):
        result = ' - ' * level + str(self.data) + '\n'
        for child in self.children:
            result += child.__str__(level+1)
        return result
    
    def addChild(self, newChild):
        self.children.append(newChild)


root_node = TreeNode('Latin',[])
spanish = TreeNode('spanish',[])
portu = TreeNode('portuguese',[])
french = TreeNode('french',[])
italian = TreeNode('italian',[])
romanian = TreeNode('romainian',[])

root_node.addChild(italian)
root_node.addChild(romanian)

italian.addChild(french)
italian.addChild(spanish)
spanish.addChild(portu)

print(root_node)