class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = 0
        subsets = []
        for i in range(len(nums)):
            n <<= 1
            n += 1
        for i in range(n+1):
            tmp = []
            index = 0
            while i:
                if i & 1:
                    tmp.append(nums[index])
                index += 1
                i >>= 1
            subsets.append(tmp)
        return subsets