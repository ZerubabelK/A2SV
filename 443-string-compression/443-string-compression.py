class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        t = chars[0]
        a = 1
        for i in chars[1:]:
            if i == t:
                a += 1
            else:
                s += t
                t = i
                if a != 1:
                    s+=str(a)
                a = 1
        s += t
        if a != 1:
            s+=str(a)
        chars[:] = [i for i in s]
        return len(s)