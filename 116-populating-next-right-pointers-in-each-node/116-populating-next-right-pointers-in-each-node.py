"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = []
        queue.append(root)
        while queue:
            n_o_nodes_cur_level = len(queue)
            prev = None
            while n_o_nodes_cur_level > 0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
                if prev != None:
                    prev.next = node
                prev = node
                n_o_nodes_cur_level -= 1
            prev.next = None
        return root
        