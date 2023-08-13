from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

def levelOrder(root:Optional[TreeNode]):
    result = []
    q = deque()
    q.append(root)

    while q: 
        levels = []
        for i in range(len(q)):
            node = q.popleft()
            if node:
                levels.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if levels:
            result.append(levels)
    return result

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(levelOrder(tree))