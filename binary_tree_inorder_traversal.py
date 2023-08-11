from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrderTraversal(root: Optional[TreeNode]):
    result = []

    def inOrder(root):
        if not root:
            return

        inOrder(root.left)
        result.append(root.val)
        inOrder(root.right)
    inOrder(root)
    return result
