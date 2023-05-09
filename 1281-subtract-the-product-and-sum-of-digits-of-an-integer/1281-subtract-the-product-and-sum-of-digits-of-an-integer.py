class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        
        if n == 1:
            return 0
        
        while n >= 1:
            remainder = n % 10
            n //= 10
            prod *= remainder
            summ += remainder
                
        return prod - summ
            