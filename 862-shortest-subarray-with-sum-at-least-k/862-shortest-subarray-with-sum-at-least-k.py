class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(n + prefix_sum[-1])
            
        index = collections.deque()
        res = len(nums) + 1
        for i, n in enumerate(prefix_sum):
            while index and n <= prefix_sum[index[-1]]:
                index.pop()
                
            while index and n - prefix_sum[index[0]] >= k:
                res = min(res, i - index.popleft())
                
            index.append(i)
            
        return res if res < len(nums) + 1 else -1