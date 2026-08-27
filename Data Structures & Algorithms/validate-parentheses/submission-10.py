class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) != 0:
                    cur = stack.pop()

                    if c == ')' and cur != '(':
                        return False
                    elif c == '}' and cur != '{':
                        return False
                    elif c == ']' and cur != '[':
                        return False
                else:
                    return False

        if len(stack) != 0:
            return False
        return True
