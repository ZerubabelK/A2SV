class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros,cur_zero,ones,cur_one,ans = 0, 0, 0, 0, 0
        for i in s:
            if i == '0':
                zeros += 1
            else:
                ones += 1
            
        for i in s:
            if i == '0':
                ans += (cur_one * (ones - cur_one))
                cur_zero += 1
            else:
                ans += (cur_zero * (zeros - cur_zero))
                cur_one += 1
                
        return ans