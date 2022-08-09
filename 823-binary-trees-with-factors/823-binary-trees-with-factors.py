class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = [1] * len(arr)
        arr.sort()
        for i in range(len(arr)):
            left = 0
            right = i - 1
            while left <= right:
                if arr[i] == arr[left] * arr[right]:
                    if left != right:
                        dp[i] += dp[left] * dp[right] * 2
                    else:
                        dp[i] += dp[left] * dp[right]
                    left += 1
                elif arr[i] < arr[right] * arr[left]:
                    right -= 1
                else:
                    left += 1
                    
        return sum(dp) % (10 ** 9 + 7)