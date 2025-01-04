def largestRectangleArea(heights: list[int]) -> int:
        n = len(heights)
        maxA = 0
        stack = []

        for i in range(n+1):
            while stack and (i==n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxA = max(maxA,height*width)
            stack.append(i)
        return maxA

heights = [7,1,7,2,2,4]
res  = largestRectangleArea(heights=heights)
print("Expected : 8")
print("Got : " + str(res))