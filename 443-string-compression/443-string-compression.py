class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        t = chars[0]
        j = 1
        for i in chars[1:]:
            print(s)
            if i == t:
                j += 1
            else:
                s += t
                t = i
                if j != 1:
                    s+=str(j)
                j = 1
        s += t
        if j != 1:
            s+=str(j)
        chars[:] = [i for i in s]
        return len(s)