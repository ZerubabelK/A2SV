class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums)
        nums += nums
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                if index < len(nums) / 2:
                    answer[index] = nums[i]
                
            stack.append(i)
        return answer