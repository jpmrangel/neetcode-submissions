class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N<=3:
            return max(nums)
        
        def dfs(i, n, cache):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = nums[i] + max(dfs(i+2, n, cache), dfs(i+3, n, cache))
            return cache[i]
        path1 = dfs(0, N-1, {})
        path2 = dfs(1, N, {})
        path3 = dfs(2, N, {})
        return max(path1, path2, path3)