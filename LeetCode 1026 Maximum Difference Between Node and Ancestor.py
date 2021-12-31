# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(curr,mini,maxi,maxidiff):
            if curr != None:
                if curr.val < mini:
                    mini = curr.val
                if curr.val > maxi:
                    maxi = curr.val
                maxidiff = max(maxidiff,dfs(curr.left,mini,maxi,maxidiff))
                maxidiff = max(maxidiff,dfs(curr.right,mini,maxi,maxidiff))
            else:
                maxidiff = max(maxidiff, abs(mini-maxi))
            return maxidiff
        diff = dfs(root,9999999999,-99999999999,0)
        return diff
