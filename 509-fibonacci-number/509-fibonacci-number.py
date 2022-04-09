class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        memo[0] = 0; memo[1] = 1

        def fibonacci(n):
            if n in memo:
                return memo[n]
            memo[n] = self.fib(n - 1) + self.fib(n - 2)
            
        fibonacci(n)
        
        return memo[n]