class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)

        for n in nums:
            if seen[n] == 1:
                return True
            seen[n] += 1
        return False

