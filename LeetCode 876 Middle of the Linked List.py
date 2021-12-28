# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = []
        curr = head
        while curr != None:
            vals.append(curr.val)
            curr = curr.next
        curr = head
        for i in range(len(vals)//2):
            curr = curr.next
        return curr
