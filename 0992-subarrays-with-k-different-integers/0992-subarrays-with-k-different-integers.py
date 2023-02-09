class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def func(nums, k):
            freq = defaultdict(int)
            l = 0
            ans = 0
            for r,i in enumerate(nums):
                if freq[i] == 0:
                    k-=1
                freq[i] +=1
                while k < 0:
                    freq[nums[l]]-=1
                    if freq[nums[l]] == 0:
                        k+=1
                    l+=1
                ans += r - l + 1
            return ans
        
        return func(nums,k) - func(nums,k-1)
    