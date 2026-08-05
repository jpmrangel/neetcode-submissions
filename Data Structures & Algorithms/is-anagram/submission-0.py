class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        ds = {}
        dt = {}

        for char in s:
            if char in ds:
                ds[char] += 1
            else:
                ds[char] = 1

        for char in t:
            if char in dt:
                dt[char] += 1
            else:
                dt[char] = 1

        for key, value in ds.items():
            if value != dt.get(key, 0):
                return False
        return True