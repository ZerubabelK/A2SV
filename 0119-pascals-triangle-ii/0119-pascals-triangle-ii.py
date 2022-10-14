class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(rowIndex+1):
            ithArr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    ithArr.append(1)
                    continue
                ithArr.append(res[-1][j] + res[-1][j - 1])
            res.append(ithArr)
        return res[-1]