class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        
        reverse = bin(n)[2:][::-1] + "0" * (32 - len(bin(n)[2:]))
        
        for i in range(len(reverse)):
            ans += int(reverse[-(i+1)]) * (2 ** i)
            
        return ans

        