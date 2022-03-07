class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [[matrix[i][0], i, 0] for i in range(len(matrix))]

        while matrix:
            minval = heappop(heap)
            
            i = minval[1]
            
            j = minval[2]+1
            
            if j < len(matrix[i]):
                heappush(heap, [matrix[i][j], i, j])
            
            
            k -= 1                
         
            if k == 0:
                return minval[0]