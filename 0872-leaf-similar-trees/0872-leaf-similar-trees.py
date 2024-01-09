# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        nodeList1 = []
        nodeList2 = []
        self.Dfs(root1, nodeList1)
        self.Dfs(root2, nodeList2)
        return nodeList1 == nodeList2

    def  Dfs(self, node, nodeList):
        if not node:
            return
        if not node.left and not node.right:
            nodeList.append(node.val)
        else:
            self.Dfs(node.left, nodeList)
            self.Dfs(node.right, nodeList)
        