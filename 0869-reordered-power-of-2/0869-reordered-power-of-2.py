class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        freq = Counter(str(n))
        power = 0
        n = int(''.join(sorted(str(n), reverse=True)))
        num = 0
        while (2 ** power) <= n:
            stringF=  Counter(str(2 ** power))
            if len(stringF) != len(freq):
                power += 1
                continue
            c = 0
            for key in stringF:
                if freq[key] == stringF[key]:
                    c += 1
            if c == len(freq):
                return True
            power += 1
        return False