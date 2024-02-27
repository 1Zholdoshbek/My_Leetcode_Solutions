# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l=[0]
        def check(node):
            if not node:
                return 0
            left=check(node.left)
            right=check(node.right)
            l[0]=max(l[0],left+right)
        
            return max(left,right)+1
        
        check(root)
        return l[0]
        
        
        
            
        