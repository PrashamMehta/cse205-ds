import collections

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_count = collections.Counter(arr)

        sorted_freq = sorted(freq_count.values(), reverse=True)

        
        min_set_size = 0
        removed_elements = 0
        total_elements = len(arr)
        half_elements = total_elements // 2

        for freq in sorted_freq:
            min_set_size += 1
            removed_elements += freq
            if removed_elements >= half_elements:
                break

        return min_set_size
