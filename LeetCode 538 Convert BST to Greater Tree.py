class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node,val):
            if not node: return val
            node.val+=dfs(node.right,val)
            return dfs(node.left,node.val)
        sum=dfs(root,0)
        return root
