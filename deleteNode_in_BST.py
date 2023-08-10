from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def deleteNode(root, key):
    #helper function
    def minValue(root):
        if root and root.left:
            root = root.left
        return root
    
    #main implementation
    if not root:
        return None
    
    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not root.right:
            return root.left
        elif not root.left: 
            return root.right
        else:
            minNode = minValue(root.right)
            root.val = minNode.val
            root.right = deleteNode(root.right, minNode.val)
    return root