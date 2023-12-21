# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(root,ans):
            if root is None:
                return
            dfs(root.left,ans)
            ans.append(root.val)
            dfs(root.right,ans)
             
        ans=[]
        dfs(root,ans)
        for i in range(1,len(ans)):
            if ans[i]<=ans[i-1]:
                return False
        return True
        
        