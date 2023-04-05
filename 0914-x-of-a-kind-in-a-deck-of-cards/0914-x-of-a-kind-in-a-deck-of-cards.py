class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck)
        f = min(counter.values())
        def findGCD(x, y):
            if y == 0:
                return x
            return findGCD(y, x % y)
        gcd = 0
        for key in counter:
            if gcd == 0:
                gcd = counter[key]
            gcd = findGCD(counter[key], gcd)
        return gcd > 1