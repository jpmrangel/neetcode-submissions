class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while True:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1
            if left >= right:
                return True

            if s[left].lower() == s[right].lower():
                left+=1
                right-=1
            else:
                return False
        
