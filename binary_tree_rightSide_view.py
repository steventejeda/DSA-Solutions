from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def rightSideView(root:Optional[TreeNode]):
    result = []
    q = deque([root])

    while q: 
        rightSide = None
        for i in range(len(q)):
             node = q.popleft()
             if node:
                rightSide = node
                q.append(node.left)
                q.append(node.right)
        if rightSide:
            result.append(rightSide.val)
    return result

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.right = TreeNode(4)
tree.left.right = TreeNode(5)

print(rightSideView(tree))