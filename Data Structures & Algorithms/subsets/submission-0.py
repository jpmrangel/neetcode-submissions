class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        i_max = len(nums)

        def check(path, i):
            if i == i_max:
                result.append(path[:])
                return
            
            path.append(nums[i])
            check(path, i+1)
            path.pop()
            check(path, i+1)
        
        check([], 0)
        return result