class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, temp: List[int]):
            if len(temp) == k:
                output.append(temp[:])
                return
            for i in range(start, n + 1):
                temp.append(i)
                backtrack(i + 1, temp)
                temp.pop()

        output: List[List[int]] = []
        temp: List[int] = []
        backtrack(1, temp)
        return output