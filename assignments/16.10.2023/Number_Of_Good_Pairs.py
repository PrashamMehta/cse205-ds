class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        unique_list = []
        for x in nums:
            if x not in unique_list:
                unique_list.append(x)
        unique_count = 0
        for y in unique_list:
            count = 0
            for z in nums:
                if y == z:
                    count+=1
            
            unique_count = unique_count + ((count * (count - 1)) // 2) 

        return unique_count
            

            
        