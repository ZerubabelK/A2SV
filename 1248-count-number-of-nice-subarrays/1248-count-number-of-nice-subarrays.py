class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        m, n = k, len(nums)
        count = 0
        prefix = [0] * (n+1)
        odd = 0

        for i in range(n):
            prefix[odd] += 1

            if nums[i] & 1:
                odd += 1

            if odd >= m:
                count += prefix[odd - m]

        return count