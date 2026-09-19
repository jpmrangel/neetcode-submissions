class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        cache = {}

        def dfs(i):
            if i >= N:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return cache[i]
        
        return max(dfs(0), dfs(1))