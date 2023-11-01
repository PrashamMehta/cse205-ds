class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a dictionary to store the next greater elements for each element in nums2
        next_greater = {}
        stack = []
        
        # Iterate through nums2 to find the next greater elements and store them in the dictionary
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Initialize the result list with -1 for all elements in nums1
        result = [-1] * len(nums1)
        
        # Fill in the result list based on the next_greater dictionary
        for i in range(len(nums1)):
            if nums1[i] in next_greater:
                result[i] = next_greater[nums1[i]]
        
        return result
