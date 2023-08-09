class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root:TreeNode, val: int) -> TreeNode:
        while root: 
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else: 
                root = root.left
        return None
    
    #Implement recursive approach
    def searchBSTRecursively(self, root: TreeNode, val) -> TreeNode:
        if not root: 
            return None

        while root: 
            if root.val == val: 
                return root
            elif val > root.val: 
                return self.searchBSTRecursively(root.right, val)
            else:
                return self.searchBSTRecursively(root.left, val)
            