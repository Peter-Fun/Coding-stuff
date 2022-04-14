class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val==val:
                return root
            if root.val>val:
                root=root.left
            else:
                root=root.right
        return None
