class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # prev, curr
        if not root:
            return
        
        head, prev = None, None
        
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
			# deal with current node
            if head == None:
                head = root
                head.left = None
            
            else:
                prev.left = None
                prev.right = root
            
            prev = root          
			# end of dealing with current node			
			
            root = root.right
        prev.left = None
        
        return head
