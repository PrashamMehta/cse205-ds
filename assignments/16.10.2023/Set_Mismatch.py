class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_counts = {}
        duplicated_num = None
        
        for num in nums:
            if num in num_counts:
                duplicated_num = num
            else:
                num_counts[num] = 1
        
        for i in range(1, n + 1):
            if i not in num_counts:
                missing_num = i
        
        return [duplicated_num, missing_num]
