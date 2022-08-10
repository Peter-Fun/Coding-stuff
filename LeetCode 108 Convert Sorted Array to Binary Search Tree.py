# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, n):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not n: return None                                           # <-- base case: leaf
        m = len(n)//2
        return TreeNode(n[m],self.sortedArrayToBST(n[:m]),              # <-- left  subtree
                             self.sortedArrayToBST(n[m+1:]))
