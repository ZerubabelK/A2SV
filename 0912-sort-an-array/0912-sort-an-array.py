class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) > 1:
                m = len(arr) // 2
                left = arr[:m]
                right = arr[m:]
                
                mergeSort(left)
                mergeSort(right)
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
                    i += 1
                    z += 1
                while j < len(right):
                    arr[z] = right[j]
                    j += 1
                    z += 1
                    
        mergeSort(nums)
        return nums