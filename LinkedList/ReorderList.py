def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #find middle
        s,f = head,head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        second = s.next
        s.next = None

        # reverse second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merge. second half might be smaller than first
        first, second = head, prev
        while second:
            tmp1,tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2