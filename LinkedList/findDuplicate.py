def findDuplicate(nums: List[int]) -> int:
        slow,fast = 0,0 
        #find where slow and fast intersect
        while True:
            slow = nums[slow] #same as slow = slow.next
            fast = nums[nums[fast]] #same as fast=fast.next.next
            if slow==fast:
                break #intersection found
        
        #floyds algo to find start of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow