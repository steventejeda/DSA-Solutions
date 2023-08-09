class TreeNode:
    def __init__(self, val):
        self.val = 0 
        self.left = None
        self.right = None

class Solution:
    def insertIntoBSTRecursively(self, root, val): 
        if not root:
            return TreeNode(val)

        if val > root.val: 
            root.right = self.insertIntoBSTRecursively(root.right, val)
        else:
            root.left = self.insertIntoBSTRecursively(root.left, val)
        return root
