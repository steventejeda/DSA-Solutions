from collections import deque, defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: Optional[TreeNode]):
    if not root:
        return None
    
    result = []
    q = deque([(0, root)])
    column_items = defaultdict(list)

    min_x = float('inf')
    max_x = float('-inf')
    
    while q:
        x, node = q.popleft()
        column_items[x].append(node.val)

        min_x = min(min_x, x)
        max_x = max(max_x, x)

        if node.left: 
            q.append((x - 1, node.left))
        if node.right:
            q.append((x + 1, node.right))
        
    for levels in range(min_x, max_x + 1):
        result.append(column_items[levels])
    
    return result

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(verticalOrder(tree))

