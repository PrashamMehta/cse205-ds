class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        score_o = score[:]

        score = sorted(score_o,reverse=True)
        for i, v in enumerate(score):
            d[v] = str(i + 1)
        ma = {"1": "Gold Medal", "2": "Silver Medal", "3": "Bronze Medal"}
        result = []
        for v in score_o:
            r = d[v]
            if r in ma:

                result.append(ma[r])
            else:
                result.append(d[v])
        return result