class Solution:
    def maxJump(self, stones: List[int]) -> int:
        max_forward = 0
        max_backward = 0
        for i in range(1, len(stones)):
            if i%2 == 0:
                max_forward = max(max_forward, abs(stones[i] - stones[i-2]))
            else:
                if i == 1:
                    max_backward = max(max_backward, abs(stones[i] - stones[0]))
                else:
                    max_backward = max(max_backward, abs(stones[i] - stones[i-2]))
                    
        return max(max_forward, max_backward)
