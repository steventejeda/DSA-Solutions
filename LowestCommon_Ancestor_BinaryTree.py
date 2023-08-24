class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None 
        

def lowestCommonAncestor(p: Node, q: Node):
    p_copy = p 
    q_copy = q 

    while p_copy != q_copy:
        p_copy = p_copy.parent if p_copy else q
        q_copy = q_copy.parent if q_copy else p
    return p_copy