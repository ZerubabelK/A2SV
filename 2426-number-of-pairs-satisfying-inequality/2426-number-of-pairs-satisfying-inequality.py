class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        ans = 0
        def findPairs(arr1, arr2):
            pairsCount = 0
            i = len(arr1) - 1
            j = len(arr2) - 1
            while i > -1:
                while j > -1 and arr2[j] >= arr1[i] - diff:
                    j -= 1
                pairsCount += len(arr2) - j - 1 if j > -1 else len(arr2)
                i -= 1
            return pairsCount
                    
        def mergeSort(arr):
            nonlocal ans
            if len(arr) > 1:
                m = len(arr) // 2
                left = arr[:m]
                right = arr[m:]
                mergeSort(left)
                mergeSort(right)
                ans += findPairs(left, right)
                i = j = z = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[z] = left[i]
                        i += 1
                    else:
                        arr[z] = right[j]
                        j += 1
                    z += 1
                while i < len(left):
                    arr[z] = left[i]
                    z += 1
                    i += 1
                while j < len(right):
                    arr[z] = right[j]
                    z += 1
                    j += 1
        mergeSort(arr)
        return ans
            