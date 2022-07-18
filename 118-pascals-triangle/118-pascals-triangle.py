class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            ithArr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    ithArr.append(1)
                    continue
                ithArr.append(res[-1][j] + res[-1][j - 1])
            res.append(ithArr)
        return res