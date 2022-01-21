class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        
        for i in nums1:
            j = nums2.index(i)
            res = [nums2[k] for k in range(j+1, len(nums2)) if nums2[k] > i]
            
            if len(res) > 0:
                ans.append(res[0])
            else: 
                ans.append(-1)
            res = []
            
        return ans