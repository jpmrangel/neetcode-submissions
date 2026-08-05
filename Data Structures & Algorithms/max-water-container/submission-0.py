class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            newArea = min(heights[l], heights[r]) * length

            if newArea > maxArea:
                maxArea = newArea
            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
            
        return maxArea