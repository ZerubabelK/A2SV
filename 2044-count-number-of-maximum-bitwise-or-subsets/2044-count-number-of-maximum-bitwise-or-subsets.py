class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = 0
        subsets = defaultdict(int)
        for i in range(len(nums)):
            n <<= 1
            n += 1
        for i in range(n+1):
            tmp = 0
            index = 0
            while i:
                if i & 1:
                    tmp |= nums[index]
                index += 1
                i >>= 1
            subsets[tmp] += 1
            
        return subsets[max(subsets.keys())]