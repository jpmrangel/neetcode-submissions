class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []
        i_max = len(nums)

        def check(i):
            if i == i_max:
                result.append(path[:])
                return
            path.append(nums[i])
            check(i+1)
            path.pop()
            check(i+1)
        
        check(0)
        return result