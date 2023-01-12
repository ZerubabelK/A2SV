    def __init__(self, n: int):
        self.m = ['f' for i in range(n)]
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        idx = 0
        for i in range(self.n):
            if self.m[i] == 'f':
                cnt += 1
            else:
                idx = i+1
                cnt = 0
            if cnt == size:
                for j in range(idx,idx+size):
                    self.m[j] = mID
                return idx
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.m[i] == mID:
                cnt += 1
                self.m[i] = 'f'
        return cnt
