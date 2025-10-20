class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        parentheses = ["(", ")", "[", "]", "{", "}"]

        stack = []
        for char in s:
            if parentheses.index(char) % 2 == 0:
                stack.append(char)
            else:
                if not stack:
                    return False
                if parentheses[parentheses.index(stack[-1])+1] != char:
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        return True
        
            