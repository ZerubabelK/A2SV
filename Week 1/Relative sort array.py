class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        newdict = dict((i,j) for j,i in enumerate(arr2))
        s=len(newdict)
        arr1.sort(key=lambda n:newdict[n] if n in newdict else s+n)    
        return arr1
