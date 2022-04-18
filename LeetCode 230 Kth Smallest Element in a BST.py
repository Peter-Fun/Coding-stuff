# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        li = []
        
        def appendelem(root):
            if root:
                appendelem(root.left)
                li.append(root.val)
                appendelem(root.right)
        
        appendelem(root)
        
        li.sort()
        
        return li[k-1]
