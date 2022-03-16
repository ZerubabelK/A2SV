class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        left = 0
        right = len(citations) - 1
        n = len(citations)
        
        while left <= right:
            mid = (left + right) // 2
            if n - mid > citations[mid]:
                left = mid + 1
            else:
                h_index = n - mid
                right = mid - 1
        return h_index