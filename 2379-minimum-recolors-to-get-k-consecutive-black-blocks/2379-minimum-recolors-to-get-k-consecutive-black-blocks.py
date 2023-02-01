class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        blacks = 0
        ans = k
        flips = 0
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                flips += 1
                blacks += 1
            if blocks[r] == 'B':
                blacks += 1
            if blacks >= k:
                ans = min(ans, flips)
                flips -= (1 if blocks[l] == 'W' else 0)
                blacks -= 1
                l += 1
         
        return ans
            