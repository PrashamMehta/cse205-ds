class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Create a dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty after processing all characters, the string is valid
        return not stack
