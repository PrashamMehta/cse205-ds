class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize the result with the first row
        result = [[1]]
        
        for i in range(1, numRows):
            # Calculate the next row based on the previous row
            previous_row = result[-1]
            new_row = [1]
            
            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])
            
            new_row.append(1)
            
            result.append(new_row)
        
        return result