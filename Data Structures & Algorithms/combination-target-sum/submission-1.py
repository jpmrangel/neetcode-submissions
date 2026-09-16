class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path = [], []
        s = 0
        N = len(nums)

        def backtracking(i_min):
            nonlocal s
            if s == target:
                result.append(path[:])
                return
            elif s > target:
                return
            for i in range(i_min, N):
                path.append(nums[i])
                s+=nums[i]
                backtracking(i)
                path.pop()
                s-=nums[i]
            
        backtracking(0)
        return result