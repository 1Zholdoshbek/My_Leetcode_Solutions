"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root == None:
            return []
        def rootF(e):
            if e.children == None:
                res.append(e.val)
            else:
                for i in e.children:
                    rootF(i)
                res.append(e.val)
        rootF(root)
        return res
        