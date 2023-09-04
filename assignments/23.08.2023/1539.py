class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1 
        missing_count = 0
        
        for num in range(1, len(arr) + k + 1):
            if num not in arr:
                missing_count += 1
                if missing_count == k:
                    return num
        
        return num + k - missing_count