class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        totalNum, sumVal, last = 0, 0, [0] * k
        for num in nums:
            last[-sumVal] += 1            
            sumVal = (sumVal+num) % k
            totalNum += last[-sumVal]

        return totalNum