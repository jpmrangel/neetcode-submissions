class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result, path = [], []
        s = 0
        N = len(candidates)

        def backtracking(i_min):
            nonlocal s
            if s == target:
                result.append(path[:])
                return
            for i in range(i_min, N):
                if s + candidates[i] > target:
                    break
                if i > i_min and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                s+=candidates[i]
                backtracking(i+1)
                path.pop()
                s-=candidates[i]
        
        backtracking(0)
        return result