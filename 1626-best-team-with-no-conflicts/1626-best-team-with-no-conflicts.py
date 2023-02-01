class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        merged = sorted(list(zip(ages, scores)))
        
        @cache
        def dp(i):
            result = 0
            for j in range(i+1, len(scores)):
                if merged[j][1] < merged[i][1]:
                    continue
                result = max(result, dp(j))
            return result + merged[i][1]
        ans = 0
        for i in range(len(ages)):
            ans = max(ans, dp(i))
            
        return ans