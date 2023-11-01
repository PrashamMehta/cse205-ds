class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        x = len(nums)
        if x>2:
            if x%2==0:
                return nums[x//2]
            return nums[(x//2)]
        else:
            return -1
        