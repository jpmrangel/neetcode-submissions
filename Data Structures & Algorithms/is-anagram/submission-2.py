class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}

        for cs, ct in zip(s, t):
            count[cs] = count.get(cs, 0) + 1
            count[ct] = count.get(ct, 0) - 1

        return all(v == 0 for v in count.values())