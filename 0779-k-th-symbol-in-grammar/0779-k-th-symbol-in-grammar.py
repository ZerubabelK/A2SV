class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recur(l, r, i):
            if l >= r:
                return i
            mid = l + (r-l) // 2
            if k > mid:
                return recur(mid+1, r, 1 if i == 0 else 0)
            else:
                return recur(l, mid, 1 if i == 1 else 0)

        return recur(1, 2 **(n-1), 0)