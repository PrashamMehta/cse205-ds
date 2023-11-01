class Solution:  
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        def quickSelect(lo: int, hi: int) -> int:
            pivot = index[lo]
            while lo < hi:
                while lo < hi and nums[index[hi]] <= nums[pivot]:
                    hi -= 1
                index[lo] = index[hi]
                while lo < hi and nums[index[lo]] >= nums[pivot]:
                    lo += 1
                index[hi] = index[lo]
            index[lo] = pivot
            return lo

        n = len(nums)
        index = list(range(n))
        
        left, right = 0, n - 1
        while left < right:
            idx = quickSelect(left, right)
            if idx < k:
                left = idx + 1
            else:
                right = idx
        
        kth_val, freq_of_kth_val = nums[index[k - 1]], 0
        for i in index[ : k]:
            if nums[i] == kth_val:
                freq_of_kth_val += 1
                
        seq = []
        for num in nums:
            if num > kth_val or num == kth_val and freq_of_kth_val > 0:
                seq.append(num)
                if num == kth_val:
                    freq_of_kth_val -= 1
        return seq