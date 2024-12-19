
def maxArea(heights : list[int]) -> int:
    res = 0
    l,r = 0,len(heights)-1
    while l<r:
        area = (r-l) * min(heights[l],heights[r])
        res = max(res,area)
        '''
        checking which index needs to be changed. Change smaller height because it becomes irrelevant when trying to maximize area
        '''
        if heights[l]<=heights[r]: #
            l+=1
        else:
            r-=1
    return res


heights=[1,8,6,2,5,4,8,3,7]
res = maxArea(heights)
print("Expected : 49")
print("Got : " + str(res))