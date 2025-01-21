def removeNthFromEnd(head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        l,r = dummy,head

        #create window of size n between l and r
        while n>0:
            r=r.next
            n-=1
        
        #shift both l and r till end of list
        while r:
            r=r.next
            l=l.next

        #delete nth node. l is pointing to (n-1)th node rn
        l.next = l.next.next

        #return actual head
        return dummy.next