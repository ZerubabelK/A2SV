class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def isSquare(x):
            square = math.sqrt(x)
            return ((square - math.floor(square)) == 0)
        
        count = 0
        stack = []
        unique = set()
        for i in range(len(nums)):
            num = nums[i]
            if num in unique:
                continue
            else:
                unique.add(num)
                stack.append((num, nums[:i] + nums[i + 1: ]))
                
        while stack:
            curr, rest = stack.pop()
            if len(rest)==0:
                count += 1
				
            unique = set()
            for i in range(len(rest)):
                num = rest[i]
                if num in unique:
                    continue
                elif isSquare(curr+num):
                    unique.add(num)
                    stack.append((num, rest[:i] + rest[i+1:]))
                    
        return count