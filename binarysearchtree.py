
# Create a Node class for creating node objects
class Node:
    
    def __init__(self, key):
        self.key = key # node has an id key
        self.left = None # node has a left node
        self.right = None # node has a right node



# function to insert a node into the binary search tree
def insert_node(node, key):
    
    # base case: if node doesn't exist, create one
    if node is None:
        return Node(key)
    # insert node into the left node    
    if key < node.key: 
        node.left = insert_node(node.left, key)
    # insert node into the right node
    else: 
        node.right = insert_node(node.right, key)
    # once node is inserted, this returns the node up through the chain
    return node


# create function that searches tree for a given key value
def tree_search(root, value):
    # if the value is less than the current node's key, move left
    if value < root.key:
        # if the left node is empty, value isn't in search tree
        if root.left is None:
            return False
        # if a node is to the left, search new node for value
        return tree_search(root.left, value)
    # if the value is greater than the current node's key, move right
    elif value > root.key:
        # if the right node is empty, value isn't in search tree
        if root.right is None:
            return False
        # if a node is to the right, search new node for value
        return tree_search(root.right, value)
    # if value is = to node key, the key has been found
    else:
        return True
        

# Testing functionality

first = Node(4)
insert_node(first, 2)
insert_node(first, 3)
print(tree_search(first, 1))
