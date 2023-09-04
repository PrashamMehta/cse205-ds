class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for word in nums:
            x = str(word)
            if(len(x)%2==0):
                count = count+1
        return count

