class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        converter_coord = lambda x, y: x * m + y
        converter_value = lambda x: (x// m, x % m)
        
        left = (0, 0)
        right = (n - 1, m - 1)
        
        while converter_coord(left[0], left[1]) <= converter_coord(right[0], right[1]):
            
            mid_value = (converter_coord(left[0], left[1]) + converter_coord(right[0], right[1]))//2
            
            mid_coord = converter_value(mid_value)
            
            i, j = mid_coord[0], mid_coord[1]
            
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] < target:
                left = converter_value(mid_value + 1)
            else:
                right = converter_value(mid_value - 1)
                
        return False
       