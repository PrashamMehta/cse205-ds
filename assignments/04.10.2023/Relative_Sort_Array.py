class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        x = []
        y = []
        for i in arr2:
             for j in arr1:
                 if j == i:
                     x.append(j)
        for j in arr1:
            if j not in arr2:
                y.append(j)
        return x+y 