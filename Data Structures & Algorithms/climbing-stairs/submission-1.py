class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return 1 if n==1 else 2
        h = [0]*n
        h[0], h[1] = 1, 2

        for i in range(2, n):
            h[i] = h[i-1] + h[i-2]
        
        return h[n-1]
        