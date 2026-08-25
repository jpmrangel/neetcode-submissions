class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        lo, hi = 0, len(heights) - 1

        while lo < hi:
            cur = min(heights[lo], heights[hi]) * (hi - lo)

            if cur > res:
                res=cur

            if heights[lo] < heights[hi]:
                lo+=1
            elif heights[lo] > heights[hi]:
                hi-=1
            else:
                lo+=1

        return res