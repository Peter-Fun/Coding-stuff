# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        crits = []
        for i in range(1, len(values)-1):
            if values[i] < values[i+1] and values[i] < values[i-1]:
                crits.append(i)
            if values[i] > values[i+1] and values[i] > values[i-1]:
                crits.append(i)
        mini = -1
        maxi = -1
        if len(crits) > 1:
            for i in range(len(crits)-1):
                if mini == -1 or crits[i+1] - crits[i] < mini:
                    mini = crits[i+1] - crits[i]
            maxi = crits[-1] - crits[0]
        return [mini,maxi]
