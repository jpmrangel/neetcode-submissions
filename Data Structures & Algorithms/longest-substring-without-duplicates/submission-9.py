class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        best = 0
        seen = {}
        while r < len(s):
            if s[r] in seen and seen[s[r]] >= l:
                l=seen[s[r]]+1
        
            seen[s[r]] = r
            best = max(best, r - l + 1)
            r+=1
        return best