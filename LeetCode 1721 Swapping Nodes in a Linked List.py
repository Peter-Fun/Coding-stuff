class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        front, last = head,head
        while k>1:
            front = front.next
            k-=1
        left = front
        while left.next!=None:
            left = left.next
            last = last.next
        front.val, last.val = last.val, front.val
        return head
