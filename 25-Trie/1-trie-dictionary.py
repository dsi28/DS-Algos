# implement Trie

class TrieNode:
    def __init__(self):
        # children is an empty dictionary
        self.children = {}
        self.endOfString = False

class Trie:
    # tc: O(1), sc: O(1)
    def __init__(self):
        self.root = TrieNode()

    # tc: O(m), sc: O(m). where m is the number of characters in the word string
    def insertWord(self,word):
        cur = self.root
        for letter in word:
            newNode = cur.children.get(letter)
            if newNode is None:
                newNode = TrieNode()
                cur.children.update({letter: newNode})
            cur = newNode
        cur.endOfString = True
        return f'successfully inserted {word}'
    
    # tc: O(m), sc: O(1)
    def searchForString(self, word):
        cur = self.root
        for letter in word:
            next_node = cur.children.get(letter)
            if next_node is None:
                return False
            cur = next_node
        
        if cur.endOfString:
            return True
        return False
    

def deleteString(root, word, index):
    letter = word[index]
    cur = root.children.get(letter)
    canThisNodeBeDeleted = False

    # cur node is shared by another letter
    if len(cur.children) > 1:
        deleteString(cur, word, index + 1)
        return False

    # checking if its the last letter in word
    if index == len(word) - 1:
        # if cur letter has a child letter change endOfString to False and return false since this node cannot be deleted
        if len(cur.children) >= 1:
            cur.endOfString = False
            return False
        # if no child letters delete curent
        else:
            root.children.pop(letter)
            return True
        
    if cur.endOfString == True:
        deleteString(cur, word, index + 1)
        return False
    
    canThisNodeBeDeleted = deleteString(cur, word, index + 1)
    if canThisNodeBeDeleted:
        root.children.pop(letter)
        return True
    else: 
        return False
        


test_trie = Trie()
result = test_trie.insertWord('waka')
print(result)
result = test_trie.searchForString('wakai')
print(result)
result = test_trie.searchForString('waka')
print(result)
result = test_trie.searchForString('wak')
print(result)
result = deleteString(test_trie.root, 'waka', 0)
print(result)