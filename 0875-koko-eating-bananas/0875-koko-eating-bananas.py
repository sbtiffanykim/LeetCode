class Solution:       
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = left + (right - left) // 2
            total = 0
            # calculate time taken to eat all
            for pile in piles: 
                if pile <= k:
                    total += 1
                else:
                    total += math.ceil(float(pile) / k)
            if total <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res