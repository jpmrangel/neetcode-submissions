class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            div=(r+l)//2
            if nums[div] == target:
                return div
            elif nums[div] < target:
                l=div+1
            else:
                r=div-1
        return -1
