class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def findDuplicate(arr):
            tortoise = arr[0]
            hare = arr[0]
            while (1):

                tortoise = arr[tortoise]

                hare = arr[arr[hare]]
                if (tortoise == hare):
                    break
            tortoise = arr[0]
            while (tortoise != hare):
                tortoise = arr[tortoise]
                hare = arr[hare]

            return tortoise
        
        return findDuplicate(nums)