class Solution(object):
    def evaluateTree(self, root):
        if not root.left and not root.right:
            if root.val == 0:
                return False
            return True
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        return left and right 