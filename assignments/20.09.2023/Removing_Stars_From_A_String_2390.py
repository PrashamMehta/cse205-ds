class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                # Check if the stack is not empty before attempting to remove characters
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
