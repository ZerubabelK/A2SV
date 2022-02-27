class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prevSum = defaultdict(int)
   
        res = 0

        currsum = 0

        for i in range(len(nums)): 
            currsum += nums[i]
            if currsum == k: 
                res += 1        

            if (currsum - k) in prevSum:
                res += prevSum[currsum - k]

            prevSum[currsum] += 1

        return res