class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        lo, hi = 0, len(heights) - 1

        while lo < hi:
            height = min(heights[lo], heights[hi])
            width = hi - lo

            cur = height * width

            if cur > res:
                res=cur

            if heights[lo] < heights[hi]:
                lo+=1
            else:
                hi-=1

        return res