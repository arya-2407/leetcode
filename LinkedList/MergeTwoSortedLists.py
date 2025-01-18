# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2
        if not cur1:
            return cur2
        if not cur2:
            return cur1
        if cur1.val <= cur2.val:
            newHead = cur1
            cur1 = cur1.next
        else:
            newHead = cur2
            cur2 = cur2.next
        cur = newHead
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur1
                cur1=cur1.next
            else:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next
        if cur2:
            cur.next = cur2
        if cur1:
            cur.next = cur1
        return newHead