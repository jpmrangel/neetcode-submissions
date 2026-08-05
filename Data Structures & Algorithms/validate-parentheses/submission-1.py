class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for b in s:
            if b == '(' or b == '{' or b == '[':
                stack.append(b)
                continue

            if len(stack) > 0:
                if b == ')' and stack.pop() != '(':
                    return False
                elif b == '}' and stack.pop() != '{':
                    return False
                elif b == ']' and stack.pop() != '[':
                    return False
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False
