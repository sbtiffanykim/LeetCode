class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = collections.Counter(stones)
        return sum([stones[j] for j in jewels if j in stones])
        