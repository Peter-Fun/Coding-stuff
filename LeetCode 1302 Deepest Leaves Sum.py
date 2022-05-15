class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = [0, 0]
        self.search(root, d, 1)
        return d[1]
    def search(self, root, d, k):
        if k == d[0]: d[1] += root.val
        elif k > d[0]: 
            d[0] = k
            d[1] = root.val
            
        if root.left != None: self.search(root.left, d, k + 1)
        if root.right != None: self.search(root.right, d, k + 1)
