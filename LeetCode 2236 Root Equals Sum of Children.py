class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return True if root.val == root.left.val + root.right.val else False
        
