class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        ans = 0
        for i in range(1,len(target)):
            string1 = target[:i]
            string2 = target[i:] 
            
            if string1 == string2:
                ans += (freq[string1]-1) * freq[string2]
            else:
                ans += freq[string1] * freq[string2]
        return ans