class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        # Create a circular array by iterating through nums twice
        for i in range(2 * n):
            # Get the actual index in the original array using modulo
            idx = i % n
            # Check if the current element is greater than the element at the index on top of the stack
            while stack and nums[idx] > nums[stack[-1]]:
                result[stack.pop()] = nums[idx]
            # Push the current index onto the stack
            if i < n:
                stack.append(idx)

        return result
