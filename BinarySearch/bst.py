def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1
        return -1

nums = [-1,0,2,4,6,8] 
target1 = 4
target2 = 5
res1 = search(nums,target1)
res2 = search(nums,target2)

print("Expected : 3")
print("Got : ", res1)

print("Expected : -1")
print("Got : ", res2)