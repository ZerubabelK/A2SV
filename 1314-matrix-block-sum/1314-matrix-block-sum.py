class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(n):
                mat[i][j] += mat[i-1][j]
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j-1]
        for i in range(m):
            for j in range(n):
                ans[i][j] += mat[min(m-1,i+k)][min(n-1,j+k)]
                if i - k - 1 >= 0:
                    ans[i][j] -= mat[i-k-1][min(n-1,j+k)]
                if j - k - 1 >= 0:
                    ans[i][j] -= mat[min(m-1,i+k)][j-k-1]
                if i - k - 1 >= 0 and j - k - 1 >= 0:
                    ans[i][j] += mat[i-k-1][j-k-1]
        return ans