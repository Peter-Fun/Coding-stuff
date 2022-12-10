# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sum(self, root):
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)
    
    def updateMax(self, x):
        self.currentMax = max(self.currentMax, (x * (self.total - x)))
    
    def dfs(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            # leaf node
            self.updateMax(node.val)
            return node.val
        currentSum = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.updateMax(currentSum)
        return currentSum
    
    def maxProduct(self, root):
        self.total = self.sum(root)
        self.currentMax = 0
        self.dfs(root.left)
        self.dfs(root.right)
        return self.currentMax % (10**9 + 7)
