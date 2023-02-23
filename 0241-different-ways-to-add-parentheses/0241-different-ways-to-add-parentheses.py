class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        input = re.split('(\+|\-|\*|\/)', expression)
        n = len(input); m = [[[] for i in range(n)] for j in range(n)]
        for i in range(1, n+1, 2):
            for j in range(0, n+1-i, 2):
                if i == 1:
                        m[j][j+i-1].append(eval(input[j]))
                else:
                    for k in range(j+1, j+i-1, 2):
                        left = m[j][k-1]; right = m[k+1][j+i-1]; operator = input[k]
                        for num1 in left:
                            for num2 in right:
                                m[j][j+i-1].append(eval(str(num1)+operator+str(num2)))
        return m[0][n-1]