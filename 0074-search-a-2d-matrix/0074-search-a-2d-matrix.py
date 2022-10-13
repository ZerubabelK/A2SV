class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.binary_search([matrix[i][0] for i in range(len(matrix))], target)
        if row < len(matrix):
            col = self.binary_search(matrix[row], target)
            if matrix[row][col] == target:
                return True
        return False
    
    def binary_search(self, arr, target, l = 0, r = -1):
        if l < 0 or r > len(arr):
            return -1
        
        r = len(arr) - 1 if r == -1 else r
        
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] > target:
                r = m - 1
            elif arr[m] < target:
                l = m + 1
            else:
                return m
        return r