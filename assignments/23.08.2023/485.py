class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in nums:
            if (i==1):
                count = count+1
                max_count = max(max_count, count)
            else:
                count = 0
            
        return max_count