class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        answer = [0] * len(nums)
        
        def findSmaller(arr1, arr2):
            pairs = 0
            i = len(arr1)-1
            j = len(arr2) - 1
            while i > -1:
                while j > -1 and arr1[i][0] <= arr2[j][0]:
                    j -= 1
                pairs += j + 1 if j > -1 else 0
                answer[arr1[i][1]] += j + 1 if j > -1 else 0
                i -= 1   
            return pairs

        def mergeSort(arr):
            if len(arr) > 1:
                m = len(arr) // 2
                left = arr[:m]
                right = arr[m:]
                
                mergeSort(left)
                mergeSort(right)
                findSmaller(left, right)
                i = j = z = 0
                while i < len(left) and j < len(right):
                    if left[i][0] < right[j][0]:
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
        return answer