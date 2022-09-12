class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        cont = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                cont += 1
            else:
                cont = 1
                
            if cont == 3:
                ans = max(ans, int(num[i]))
                cont = 1
        if ans > -1:
            return ''.join([str(ans) for i in range(3)])
        else:
            return ''