import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in nums
        counter = collections.Counter(nums)
        
        # Use a min-heap to maintain the k most frequent elements
        min_heap = []

        # Iterate through the elements and maintain a heap of size k
        for num, freq in counter.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if freq > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (freq, num))
        
        # Extract the k most frequent elements from the heap
        result = [num for _, num in min_heap]

        return result
