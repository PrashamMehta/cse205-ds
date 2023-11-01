class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)-1
        for i in range (n):
            swap = False
            for j in range (n-i):
                if nums[j]>nums[j+1]:
                    x = nums[j+1]
                    nums[j+1]= nums[j]
                    nums[j]= x
                    swap = True 
            if not swap :
                break
        return (nums[-1]-1)*(nums[-2]-1)