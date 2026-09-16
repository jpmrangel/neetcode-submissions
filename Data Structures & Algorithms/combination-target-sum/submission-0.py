class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path = [], []
        s = 0
        i_max = len(nums)
        # [2, 5, 6, 9]

        def backtracking(i_min):
            nonlocal s
            if s == target:
                result.append(path[:])
                return
            elif s > target:
                return
            for i in range(i_min, i_max):
                path.append(nums[i])
                s+=nums[i]
                backtracking(i)
                path.pop()
                s-=nums[i]
            
        backtracking(0)
        return result