class Solution(object):
    def sortSentence(self, s):
        s = s.split()
        s.sort(key = lambda val: val[-1])
        s=" ".join([i[:-1] for i in s])
        return s