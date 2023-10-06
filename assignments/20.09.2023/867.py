class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x = []
        a = len(matrix) #for rows
        b = len(matrix[0]) #for columns

        for i in range(b):
            arr = []
            for j in range(a):
                arr.append(matrix[j][i])
            x.append(arr)
        return x