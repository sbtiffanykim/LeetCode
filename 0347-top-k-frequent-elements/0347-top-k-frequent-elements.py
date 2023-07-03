class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = collections.Counter(nums)
        freq = nums.most_common(k)
               
        return [f[0] for f in freq]
        