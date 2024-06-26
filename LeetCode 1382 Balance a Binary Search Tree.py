# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        values = []
        def populate(r):
            if r is None:
                return
            populate(r.left)
            values.append(r.val)
            populate(r.right)
        def maketree(l,r):
            if l > r:
                return None
            left = maketree(l,(l+r)/2 - 1)
            right = maketree((l+r)/2 + 1, r)
            node = TreeNode(values[(l+r)/2], left, right)
            return node
        populate(root)
        return maketree(0,len(values)-1)
        
