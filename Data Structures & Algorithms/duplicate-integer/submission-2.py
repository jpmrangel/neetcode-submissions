class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            if seen.get(n, 0) == 0:
                seen[n] = 1
            else:
                return True
        return False

