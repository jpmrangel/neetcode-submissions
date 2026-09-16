class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return 1 if n==1 else 2
        a, b, c = 1, 2, 0
        for i in range(2, n):
            end = a + b
            a, b = b, end
        return end
        