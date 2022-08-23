class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(len(nums)):
            curr = max(curr, nums[i])
            
            if not curr and i < len(nums) - 1:
                return False
            
            curr -= 1
            
        return True