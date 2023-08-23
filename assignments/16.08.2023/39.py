class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  

        for num in candidates:
            for t in range(num, target + 1):
                for combo in dp[t - num]:
                    dp[t].append(combo + [num])

        return dp[target]