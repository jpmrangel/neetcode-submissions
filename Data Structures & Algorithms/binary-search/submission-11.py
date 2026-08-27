class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if l == r:
            if nums[0] == target:
                return 0
            else:
                return -1

        div = r//2
        while r-l>1:
            if nums[div] == target:
                return div
            elif nums[div] > target:
                r=div
            else:
                l=div
            div = l + (r-l)//2
        if nums[l]==target:
            return l
        elif nums[r]==target:
            return r
        return -1
