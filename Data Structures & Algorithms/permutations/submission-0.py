class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        N = len(nums)
        included = [False]*N

        def backtracking(i):
            if i==N:
                result.append(path[:])
                return

            for idx, val in enumerate(included):
                if not val:
                    path.append(nums[idx])
                    included[idx] = True
                    backtracking(i+1)
                    path.pop()
                    included[idx] = False

        backtracking(0)
        return result