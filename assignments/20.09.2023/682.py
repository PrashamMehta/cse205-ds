class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == 'C':
                stack.pop()  # Remove the last valid score
            elif op == 'D':
                stack.append(2 * stack[-1])  # Double the last score
            elif op == '+':
                stack.append(stack[-1] + stack[-2])  # Add the sum of the last two scores
            else:
                stack.append(int(op))  # Convert the string to an integer and add it to the stack
        
        return sum(stack)
